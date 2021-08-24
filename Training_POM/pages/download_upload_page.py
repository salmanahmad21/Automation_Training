from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re
from pages.row_page import Methods


file_name = "leo_astrology_sign.jpeg"
download_id = "downloadButton"
upload_id = "uploadFile"
upload_path = "/Users/salmanahmad/Downloads/Selenium_Training/leo_astrology_sign.jpeg"
upload_get_text_id = "uploadedFilePath"


upload_text = (By.ID, upload_get_text_id)


class UploadDownloadMethods:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": "/Users/salmanahmad/Downloads/Selenium_Training"}
        options.add_experimental_option("prefs", preferences)
        print("Working")
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver", chrome_options=options)
        self.driver.get(url)

    def click(self, locator):

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, locator))).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, locator))).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)).text

    def waiting(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return element.text








