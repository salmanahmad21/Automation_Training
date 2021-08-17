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

    def test_switch_url(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")

        driver.get("https://demoqa.com/links")
        tab_link = driver.find_element_by_id("simpleLink")
        tab_link.click()
        time.sleep(2)
        parent_window = driver.current_window_handle
        child_window = driver.window_handles
        for view in child_window:
            if view != parent_window:
                driver.switch_to.window(view)
                if driver.find_element_by_class_name("home-body"):
                    print("Home Class Exist in new tab")
                else:
                    print("Not Found")
                break
            time.sleep(3)


if __name__ == "__main__":
    unittest.main()
