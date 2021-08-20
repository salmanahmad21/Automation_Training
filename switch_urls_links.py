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
import numpy as n


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get("https://demoqa.com/links")
        time.sleep(2)

    def test_switch_url(self):
        driver = self.driver

        tab_link = driver.find_element_by_id("simpleLink")
        tab_link.click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        get_class_name = driver.find_elements_by_class_name(
            "home-body")[0].get_attribute('class')
        print(get_class_name)
        time.sleep(2)
        if get_class_name == "home-body":
            print("Home-Body Class Found")
        else:
            print("Class not found")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
