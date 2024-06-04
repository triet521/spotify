from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

s = Service(r'C:\Users\triet\chromedriver.exe')
options = Options()
options.add_argument(r"user-data-dir=C:\\Users\\triet\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 4")
driver = webdriver.Chrome(service=s, options=options)
driver.get("http://127.0.0.1:5000/")
time.sleep(3)
button = driver.find_element(By.XPATH, '//*[@id="encore-web-main-content"]/div/main/section/div/div/div[5]/button')
button.click()
time.sleep(10)
