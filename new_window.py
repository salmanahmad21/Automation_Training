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
        self.driver.get("https://demoqa.com/browser-windows")
        time.sleep(2)

    def test_new_window(self):
        driver = self.driver
        window_before = driver.window_handles[0]
        new_window_btn = driver.find_element_by_id("windowButton")
        new_window_btn.click()
        time.sleep(1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        get_text = driver.find_element_by_id("sampleHeading").text
        print(get_text)
        self.assertEqual("This is a sample page", get_text,
                         "Text Not Match - Test Failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
