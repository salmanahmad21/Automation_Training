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
        i = 1
        while i <= 4:
            btn = driver.find_element_by_css_selector(
                f"[id=verticalListContainer]> li:nth-child({i})")
            btn.click()
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    unittest.main()
