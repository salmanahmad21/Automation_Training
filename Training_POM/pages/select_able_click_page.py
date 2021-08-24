from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re

get_total_clickAbles = "#verticalListContainer>li"



class ClickAblesMethod:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get(url)

    def total_click_able(self, locator):
        list_of_click_ables = self.driver.find_elements_by_css_selector(locator)
        print(list_of_click_ables)
        return list_of_click_ables

    def get_all_class_name(self, click_able):
        all_class_names = []
        after_click = []
        for i in range(len(click_able)):
            all_class_names.append(click_able[i].get_attribute("class"))
            self.driver.find_elements_by_css_selector(
                "#verticalListContainer>li")[i].click()
        return all_class_names

    def after_click_class_name(self, click_able):
        after_click = []
        for i in range(len(click_able)):
            after_click.append(click_able[i].get_attribute("class"))
        return after_click






