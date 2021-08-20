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
        self.driver.get("https://demoqa.com/webtables")
        time.sleep(2)

    def test_add_row(self):
        driver = self.driver
        add_btn = driver.find_element_by_id("addNewRecordButton")
        add_btn.click()
        time.sleep(1)
        input_data = ["Salman", "Ahmad",
                      "Sulmanmansha@gmail.com", "27", "200000", "Engineering"]
        input_ids = ["firstName", "lastName",
                     "userEmail", "age", "salary", "department"]
        for i in range(len(input_ids)):
            driver.find_element_by_id(
                f"{input_ids[i]}").send_keys(f"{input_data[i]}")
            time.sleep(1)
        time.sleep(3)
        submit_btn = driver.find_element_by_id("submit")
        submit_btn.click()
        time.sleep(3)
        total_records = driver.find_elements_by_css_selector(
            '.action-buttons span:nth-child(2)')
        if len(total_records) > 3:
            print("New Record Added")
        else:
            print("Record Not Added")

    def test_search_record(self):
        search_value = "39"
        driver = self.driver
        search_input = driver.find_element_by_id("searchBox")
        search_input.send_keys(f"{search_value}")
        time.sleep(1)
        find_record = driver.find_elements_by_class_name("rt-td")
        value = []
        for i in range(12):
            value.append(find_record[i].text)
        j = 0
        for j in range(len(value)):
            if value[j] == search_value:
                print("Value Matched in index")

    def test_delete(self):
        driver = self.driver
        delete_rows_ids = ['delete-record-1',
                           'delete-record-2', 'delete-record-3']
        available_ids = driver.find_elements_by_css_selector(
            '.action-buttons span:nth-child(2)')
        for i in range(len(available_ids)):
            delete_row = driver.find_element_by_id(f"{delete_rows_ids[i]}")
            delete_row.click()
            time.sleep(2)

        remaining_ids = driver.find_elements_by_css_selector(
            '.action-buttons span:nth-child(2)')

        self.assertEqual(
            0, len(remaining_ids), "IDs Not Deleted - Test Failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
