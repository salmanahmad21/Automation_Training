from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.common.alert import Alert

prompt_input_value = "Salman"
first_btn_id = "alertButton"
second_btn_id = "timerAlertButton"
third_btn_id = "confirmButton"
forth_btn_id ="promtButton"
get_result_text = "confirmResult"
prompt_result_text_id = "promptResult"
third_btn_expected_result = "You selected Cancel"



class AlertsMethods:

    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get(url)

    def accept_wait_alerts(self):
        try:
            WebDriverWait(self.driver, 7).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except (Exception, ValueError, TimeoutError, Exception):
            return None

    def dismiss_wait_alerts(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except (Exception, ValueError, TimeoutError, Exception):
            return None
    def promt_wait_alerts(self, keys):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.send_keys(keys)
            alert.accept()
        except (Exception, ValueError, TimeoutError, Exception):
            return None

    def click(self, locator):

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, locator))).click()

    def waiting(self, locator):
        try:
            WebDriverWait(self.driver, 6).until(EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, locator))).text

    def clean_text(self, original, expected):
        result = original.replace(original, expected)
        return result


    def tearDown(self):
        self.driver.close()
