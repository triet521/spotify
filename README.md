# spotify
Spotify Listening History with Spotify API

- My first project in attempt to automate the progress of pulling data from Spotify API and visualize them with Excel Pivot Table. 
- In the future I may cooporate AI to read my listening history and give me my overall mood that week.
- newpyt.py is the script to pull data from Spotify API so run that first, then run autoclick.py to automate the clicking progress (when Authorize window pops up)
- Because in autoclick.py I include a code to run Selenium with my Chrome Profile that has logged in to Spotify (smooth out the Authorize progress) so to things work out for you, you have to find your own Chrome Proflie and edit the code.
I will include a code that log in automatically in the future. I wrote this code to myself so I dont worry to much about availability.
- 2nd.csv is the data .csv file. Because when we update .csv file, all kinds of format in there will be resetted so I have to move the visualization part to another file, which is Visualize.xlsx
(I tried changing to .xlsx but yield no result, maybe in the future I will find a way to fuse them into 1 .xlsx file, as I want to do the same with 2 .py files above)
- In Visualize.xlsx in the Reminder sheet, the date is displayed thanks to a new measure I added into Power Pivot so that sheet may not display properly.
I will include some images to give you a better understanding about that sheet.

