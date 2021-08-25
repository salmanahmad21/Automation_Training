from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

yes_btn_id = "#yesRadio"
# impressive_btn_id = (By.ID, "impressiveRadio")
result_text_class = (By.CLASS_NAME, "text-success")


class RadioMethods:
    def __init__(self, driver):
        self.driver = driver
        

    def yes_javascript_click(self, locator):
        javascript = f"document.querySelector({locator}).click()"
        self.driver.execute_script(javascript)
