import spotipy
from spotipy import Spotify
from spotipy.cache_handler import FlaskSessionCacheHandler
from spotipy.oauth2 import SpotifyOAuth 
import flask
from flask import Flask, request, redirect, session, url_for
import os
from spotipy import SpotifyClientCredentials
import pandas as pd
import json
import pandas
from selenium import webdriver
import time 
from selenium.webdriver.edge.service import Service
from multiprocessing import Process
import subprocess 

app = Flask(__name__)
app.secret_key= os.urandom(64)

client_id = 'e1a2661e5da14f56bf91ae931a3a20b1'
client_secret = 'e7cb3f7571864a23bae16147f9def040'
scope = 'user-read-recently-played'

redirect_url = 'http://localhost:5000/callback'
token_url = 'https://accounts.spotify.com/api/token'
auth_url = 'https://accounts.spotify.com/authorize'
api_url = 'https://api.spotify.com/v1/'

cache_handler = FlaskSessionCacheHandler(session)
oauth = SpotifyOAuth(
    client_id = client_id,
    client_secret= client_secret,
    scope= scope,
    redirect_uri= redirect_url,
    cache_handler= cache_handler,
    show_dialog=True
)
sp = Spotify(auth_manager=oauth)

@app.route('/')
def index():
    if not oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('access'))

@app.route('/callback')
def callback():
    oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_played'))  

@app.route('/get_played')
def get_played():
    if not oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = oauth.get_authorize_url()
        return redirect(auth_url)
    played = sp.current_user_recently_played()
    data = json.dumps(played)
    data1 = json.loads(data)

    #Pull các cột cần sử dụng từ file JSON
    cleaned = []
    for t in data1['items']:
        cleaned.append({'Artist': t['track']['artists'][0]['name'],
                        'Album': t['track']['album']['name'],
                        'Song': t['track']['name'],
                        'Release date': t['track']['album']['release_date'],
                        'Album type': t['track']['album']['album_type'],
                        'Song duration': t['track']['duration_ms'],
                        'Date&time played': t['played_at']
                      })
    test1 = pd.DataFrame(cleaned)

    #Download file .csv về máy nếu chưa có file
    #test1.to_csv(r"C:\\Users\\triet\\Desktop\\2nd.csv")    
    #return redirect('/finish')

    with open(r'C:\\Users\\triet\\\Desktop\\2nd.csv', 'r+') as f: # open file as read/append
        f.seek(0, 2)          # go to end of file
        f.seek(f.tell()-1, 0) # come back one character
        if f.read() != '\n':  # if last character is not \n
            f.write('\n')     # then append \n

    #Update dữ liệu cho file .csv có trong máy 
    test1.to_csv(r'C:\\Users\\triet\\\Desktop\\2nd.csv', mode='a', index= False, header= False, encoding='utf-8') 
    return redirect('/finish')

#Màn hình thông báo pull JSON từ API thành công
@app.route('/finish')
def finish():
    return "Finished downloading data"

if __name__ == '__main__':
    app.run(debug=True)
    
    
