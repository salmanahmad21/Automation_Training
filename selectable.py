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

    def test_clickable_clicks(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")
        driver.get("https://demoqa.com/selectable")
        time.sleep(3)
        old_list = driver.find_elements_by_css_selector(
            "#verticalListContainer>li")
        i = 1
        for i in range(len(old_list)):
            print(i)

            names = old_list[i].get_attribute("class")

            btn = driver.find_element_by_css_selector(
                f"[id=verticalListContainer]> li:nth-child({i+1})")
            btn.click()
            time.sleep(1)

            new_list = driver.find_elements_by_css_selector(
                "#verticalListContainer>li")
            new_names = new_list[i].get_attribute("class")

            time.sleep(1)
            if new_names != names:
                print("Verified Already Clicked")
            else:
                print("Not Clicked")


if __name__ == "__main__":
    unittest.main()
