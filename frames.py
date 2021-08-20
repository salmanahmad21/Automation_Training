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
        self.driver.get("https://demoqa.com/frames")
        time.sleep(2)

    def test_frames(self):
        driver = self.driver
        driver.switch_to.frame("frame1")
        frame1_text = driver.find_element_by_id("sampleHeading").text
        print("Text From Page 1 >>> ", frame1_text)
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to.frame("frame2")
        frame2_text = driver.find_element_by_id("sampleHeading").text
        print("Text From Page 2 >>> ", frame2_text)
        self.assertEqual(frame1_text, frame2_text,
                         "Text Are Not Matching - Failed")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
