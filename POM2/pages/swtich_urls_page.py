from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re


tab_link_id = (By.ID, "simpleLink")
home_class = "home-body"



class SwitchMethods:
    def __init__(self, driver):
        self.driver = driver

    def switch_tabe(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def class_name_index(self, locator):
        return self.driver.find_elements_by_class_name("home-body")[0].get_attribute('class')

