#! /usr/bin/env python3
# Serafina Yu
# @serafinayu
#
# This is for me to try out different selenium functions
#


# webdriver module provides all WebDriver implementations like Firefox, Chrome, IE, and Remote
from selenium import webdriver
# keys class provides keys on the keyboard like RETURN, F1, ALT, etc
from selenium.webdriver.common.keys import Keys
# by class used to locate elements within document
from selenium.webdriver.common.by import By

# Set an instance of Chrome WebDriver
driver = webdriver.Chrome()
# driver,get will navigate to the provided URL and wait until the page is fully loaded before returning control to the rest of the script
driver.get("https://www.target.com/s?searchTerm=tide&tref=typeahead%7Cterm%7Ctide%7C%7C%7Chistory")
# Assert an error if "Target" is not in the title 
assert "Target" in driver.title
# Finds the element in the DOM with name "last"
# Refer here for the rest of the element attributes: https://sele    nium-python.readthedocs.io/locating-elements.html#locating-elements
elem = driver.find_element(By.CLASS_NAME, "iZqUcy")
print(elem)
# Process for sending keyboard keys as inputs:
# Clear any pre-populated text in the input field 
elem.clear()
# Send the text "pycon" into the input field 
# elem.send_keys("pycon")

# Hit return so that the form submits
# elem.send_keys(Keys.RETURN)
# After submission of the page, raise this assertion if there are no results
assert "No results found." not in driver.page_source
# Close the browser window once done
driver.close()

