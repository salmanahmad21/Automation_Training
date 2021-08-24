from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

add_btn_id = "addNewRecordButton"
status_of_values = "div[class='action-buttons'] span:nth-child(2)"
submit_btn_id = "submit"
form_values = ["firstName", "lastName", "userEmail", "age", "salary", "department"]
form_input_data = ["Salman", "Ahmad", "sulmanmansha@gmail.com", "27", "20000", "CsIT"]
ids = ["delete-record-1", "delete-record-2", "delete-record-3"]
search_value = "39"
search_box_id = "searchBox"
find_record = "rt-td"
value = []


class Methods:

    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get(url)

    def click(self, locator):

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, locator))).click()

    def click_css_selector(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def click_class_name(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, locator))).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, locator))).send_keys(text)

    def all_elements(self, locator):
        self.driver.find_elements_by_css_selector(locator)

    def all_elements_class_name(self, locator):
        return self.driver.find_elements_by_class_name(locator)

    def click_css_selector(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)).text

    def waiting(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()


    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return element.text
