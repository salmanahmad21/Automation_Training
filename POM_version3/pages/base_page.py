from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)).click()
        except:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)).click()

    def send_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)).text

    def wait_for_ele_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_all_elements(self, locator):
        try:
            return self.driver.find_elements_by_class_name(locator)
        except:
            return self.driver.find_elements_by_css_selector(locator)

    def get_element_property(self, locator):
        ele = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return ele

    def clean_text(self, original, expected):
        result = original.replace(original, expected)
        return result


