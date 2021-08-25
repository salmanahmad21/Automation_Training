from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)).click()

    def click2(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)).text

    def waiting(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_len_all_elements(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    def click_return(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator))

    def all_elements(self, locator):
        self.driver.find_elements_by_css_selector(locator)

