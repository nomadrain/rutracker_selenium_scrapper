# Scrapping example for the Rutracker
Scrapping the rutracker torrents tracker using Python selenium and BeautifulSoup. Works in headless mode (without brouser window) and can be used without graphic display.

## Requirements
- Python3
- Google Chrome
- libraries: json, selenium, bs4, fake_useragent

## Install and configure

1. Clone the repository

```
git clone https://github.com/nomadrain/rutracker_selenium_scrapper.git
```

2. Install the Python dependencies: json, selenium, bs4, fake_useragent

3. Create a file creds.py in the same directory
```
cd rutracker_selenium_scrapper
touch creds.py
```

4. Modify creds.py to include your RuTracker credentials
```
rutrackername = 'username'
rutrackerpass = 'userpass'
```

## Run it

Run the application and examine the new files:
```
python ./rutracker.py
rutracker_search_result.html
all_2021_rutracker_moview.json
```
