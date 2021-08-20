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
from selenium.webdriver.common.alert import Alert


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")
        self.driver.get("https://demoqa.com/alerts")
        time.sleep(2)

    def test_alerts(self):
        prompt_input_value = "Salman"
        driver = self.driver
        time.sleep(1)
        first_btn = driver.find_element_by_css_selector("[id=alertButton]")
        first_btn.click()
        time.sleep(1)
        accept_alert = driver.switch_to.alert
        accept_alert.accept()
        time.sleep(1)
        second_btn = driver.find_element_by_id("timerAlertButton")
        second_btn.click()
        time.sleep(6)
        accept_alert2 = driver.switch_to.alert
        accept_alert2.accept()
        third_btn = driver.find_element_by_id("confirmButton")
        third_btn.click()
        time.sleep(1)
        cancel_alert = driver.switch_to.alert
        cancel_alert.dismiss()
        time.sleep(1)
        result_text = driver.find_element_by_id("confirmResult").text
        self.assertEqual("You selected Cancel", result_text,
                         "Text Not Matched - Failed")
        forth_btn = driver.find_element_by_id("promtButton")
        forth_btn.click()
        time.sleep(1)
        prompt_alert = driver.switch_to.alert
        time.sleep(1)
        prompt_alert.send_keys(f"{prompt_input_value}")
        time.sleep(1)
        prompt_alert.accept()
        time.sleep(5)
        prompt_result_text = driver.find_element_by_id("promptResult").text
        clean_prompt_result = prompt_result_text.replace(
            prompt_result_text, prompt_input_value)
        self.assertEqual(clean_prompt_result, prompt_input_value,
                         "Text Not Match - Failed")

        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
