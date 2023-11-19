#! /usr/bin/env python3

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

def main():
    driver = webdriver.Chrome()

if __name__ == '__main__':
    main()
