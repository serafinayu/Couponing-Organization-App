#!/usr/bin/env python3

# Webscraper for Target.com
# Get the URL to access all participating items for the promotion/deal
# Find the specific div element that links to the promoted item
# For each option/size variety the listing has
    # Look for element with the promotion listed under it
        # If promotion element found
            # Add item name, size variation, and price to database
        #  If promotion element not found
            #  Go to next variation
    #  After scraping through all options/variations of an item
        #  Go back to all participating items in promotion and grab the next item on the list

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


URL = "https://www.target.com/pl/130998525?moveTo=432product-list-grid"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
allListings = soup.find_all("div", class_="dOpyUp")
# allListings = soup.find_all("div", class_="qwCgKJ")

# Selenium Simple Usage


for listing in allListings:

    print(listing.text, end="\n"*2)
    
print(allListings)