#!/usr/bin/env python

"""
Author: Nomad Rain / nomadrain@gmail.com.


"""

import sys
import time
import random
import traceback
import json
import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from creds import rutrackername, rutrackerpass


def main():
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.chrome}")
    options.headless = True
    
    try:
        thepage = ''
        browser = webdriver.Chrome(executable_path="./chrome/chromedriver", options=options)
        browser.get(url='https://rutracker.org/forum/index.php')
        time.sleep(random.randrange(3, 5))
        
        if not os.path.exists("rutracker_cookies.pkl"):
            # Click the 'Enter' button
            enter_link_xpath = '/html/body/div[4]/div[1]/div[1]/div[3]/table/tbody/tr/td/div/a[2]/b'
            browser.find_element_by_xpath(enter_link_xpath).click()
            time.sleep(random.randrange(3, 5))
            
            username_input = browser.find_element_by_name('login_username')
            username_input.clear()
            username_input.send_keys(rutrackername)
            
            time.sleep(5)
            
            password_input = browser.find_element_by_name('login_password')
            password_input.clear()
            password_input.send_keys(rutrackerpass)
            
            password_input.send_keys(Keys.ENTER)

            # Sleeping for not to be bunned
            time.sleep(5)

            # Stopping the page loading because of adds.
            browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
            
            # Saving cookies with active login
            pickle.dump(browser.get_cookies(), open("rutracker_cookies.pkl", "wb"))
        
        else:
            cookies = pickle.load(open("rutracker_cookies.pkl", "rb"))
            for cookie in cookies:
                browser.add_cookie(cookie)
        
        # Sleeping for not to be bunned
        time.sleep(5)
        browser.get('https://rutracker.org/forum/tracker.php?f=1950')
        thepage = browser.page_source
        
        # Saving intermediate results
        with open("rutracker_search_result.html", "w") as rt:
            rt.write(thepage)
        
        # Reading from the local file to have a possibility to remove the
        # above code
        with open("rutracker_search_result.html", "r") as rt:
            thepage = rt.read()
        
        soup = BeautifulSoup(thepage, "lxml")
        links = soup.find_all(name="a", attrs={"class": "med tLink ts-text hl-tags bold"})
        
        all_movies = []
        i = 0
        for item in links:
            item_text = item.text
            item_href = "https://rutracker.org/forum/" + item.get("href")
            i += 1
            all_movies.append((item_text, item_href))
        
        with open("all_2021_rutracker_moview.json", "w") as file:
            json.dump(all_movies, file, indent=4, ensure_ascii=False)
    
    except Exception as ex:
        print(traceback.format_exc())
        print(ex)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(traceback.format_exc())
        print(str(err) + ' - this error caught in the main:except block')
        sys.exit(2)
