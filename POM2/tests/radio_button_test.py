from selenium import webdriver
from pages.rows_page import *
from pages.base_page import *
from pages.swtich_urls_page import *
from pages.radio_button_page import *

import unittest


class RadioButtons(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")


    def test_radio_button(self):
        self.driver.get("https://demoqa.com/radio-button")
        func = CommonMethods(self.driver)
        radio_func = RadioMethods(self.driver)
        radio_func.javascript_click(yes_btn_id)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
