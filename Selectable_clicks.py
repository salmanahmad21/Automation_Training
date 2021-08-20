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
        self.driver.get("https://demoqa.com/selectable")
        time.sleep(2)

    def test_clickables(self):
        driver = self.driver
        total_click_able = driver.find_elements_by_css_selector(
            "#verticalListContainer>li")
        old_class_names = []
        after_click_class_names = []
        for i in range(len(total_click_able)):
            old_class_names.append(
                total_click_able[i].get_attribute("class"))
            driver.find_elements_by_css_selector(
                "#verticalListContainer>li")[i].click()
            time.sleep(1)
            after_click_class_names = []
            after_click = driver.find_elements_by_css_selector(
                "#verticalListContainer>li")
            for i in range(len(after_click)):
                names = after_click[i].get_attribute("class")
                after_click_class_names.append(names)
        print("OLD Class Names >>> ", old_class_names)
        print("After click Class names >>> ", after_click_class_names)
        if old_class_names != after_click_class_names:
            print("Class Names Updated - Click Performed")
        else:
            print("Class Name Not Changed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
