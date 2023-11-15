#! /usr/bin/env python3
# Serafina Yu
# CPSC 386-02
# 2023-02-12
# serafyu@csu.fullerton.edu
# @serafinayu
#
# Project: Webscraper for Target.com
#
# This is a webscraper meant to scrape information from Target.com for extreme couponing uses
#

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
# Module provides all WebDriver implementations like Firefox, Chrome, IE, and Remote
from selenium import webdriver
# Allows the use of keyboard keys as inputs
from selenium.webdriver.common.keys import Keys
# Allows search of DOM elements by using classes, ids, names, etc
from selenium.webdriver.common.by import By
# Lets page fully load before grabbing HTML data
from selenium.webdriver.support.wait import WebDriverWait
# Used in conjunction with the wait module: waits for expected conditions
from selenium.webdriver.support import expected_conditions as EC

""" Main function """


def main():
    """URL that will be scraped"""
    URL = "https://www.target.com/s?searchTerm=tide&tref=typeahead%7Cterm%7Ctide%7C%7C%7Chistory"

    """
        Beautiful soup - send a get request for this URL and the server will
        send back & store the HTML data in the page variable.

        I will be using selenium since beautiful soup cannot wait for the
        entire page to load before grabbing the elements
    """
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # allListings = soup.find_all("div", class_="qwCgKJ")

    """ Set a Selenium instance of Chrome WebDriver """
    # Set an instance of Chrome WebDriver
    driver = webdriver.Chrome()
    # Navigate to the provided URL and wait til the page is fully loaded before returning control to the rest of the script
    driver.implicitly_wait(20)
    driver.get(URL)
    # Assert an error if "Target" is not in the title
    assert "Target" in driver.title
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    for x in range(0,2):
        body.send_keys(Keys.PAGE_DOWN)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        elements = driver.find_elements(By.CLASS_NAME, "cbOry")
        # elements = driver.find_elements(By.CLASS_NAME, "dOpyUp")
        count = 0
        for item in elements:
            print(count, item.text)
            count += 1
    # except:
    #     print("An error occured. Closing.")
    finally: 
        # Close the browser window once done
        driver.close()
    # try:
    #     # Find all elements with the following class name
    #     elem = driver.find_element(By.CLASS_NAME, 'iZqUc')
    #     print(elem.text)
    # except:
        # print("An error occured. Closing.")
    # After submission of the page, raise this assertion if there are no results
    # assert "No results found." not in driver.page_source


# async def scrollDown(driver, URL):
#     await driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


""" Execute main program """

if __name__ == '__main__':
    main()
