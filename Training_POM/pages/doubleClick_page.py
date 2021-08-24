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

double_click_id = "doubleClickBtn"
right_click_id = "rightClickBtn"
simple_click = ".col-12.mt-4.col-md-6 .mt-4:nth-of-type(3)> button"



class DoubleClickMethod:

    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get(url)

    def click_by_css_selector(self, locator):
        self.driver.find_element_by_css_selector(locator).click()

    def click_by_id(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, locator)))

    def Double_click_actions(self, click_btn):
        driver = self.driver
        action = ActionChains(driver)
        action.double_click(on_element=click_btn)
        action.perform()

    def Right_click_actions(self, click_btn):
        driver = self.driver
        action = ActionChains(driver)
        action.context_click(on_element=click_btn)
        action.perform()
