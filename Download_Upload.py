from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Update Preferences For Download Location
options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": "/Users/salmanahmad/Downloads/Selenium_Training"}
options.add_experimental_option("prefs", preferences)

# Lunch Browser
driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver", chrome_options=options)

driver.get("https://demoqa.com/upload-download")

# Download File
download = driver.find_element_by_css_selector("[id=downloadButton]")
download.click()


# Upload File

upload = driver.find_element_by_css_selector("input[id=uploadFile]")
upload.send_keys(
    "/Users/salmanahmad/Downloads/Selenium_Training/leo_astrology_sign.jpeg")
