from selenium import webdriver
from pages.row_page import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

import unittest


class RowsTest(unittest.TestCase):

    def test_add_row(self):
        url = "https://demoqa.com/webtables"
        clicker = Methods(url)
        clicker.click(add_btn_id)
        for i in range(len(form_input_data)):
            clicker.send_keys(form_values[i], form_input_data[i])
            time.sleep(4)
        self.assertGreater(len(status_of_values), 3, "New Value is not added in form")

    def test_delete_row(self):
        url = "https://demoqa.com/webtables"
        clicker = Methods(url)

        for i in range(len(ids)):
            clicker.click(ids[i])
        remaining_ids = clicker.all_elements(status_of_values)
        if not remaining_ids:
            status = False

        self.assertEqual(
            False, status, "IDs Not Deleted - Test Failed")

    def test_search_record(self):
        url = "https://demoqa.com/webtables"
        clicker = Methods(url)
        clicker.send_keys(search_box_id, search_value)
        result = clicker.all_elements_class_name(find_record)

        target = ""
        for i in range(len(result)):
            value.append(result[i].text)
        j = 0
        for j in range(len(value)):
            if value[j] == search_value:
                target = value[j]
                print("Value Matched in index")

        self.assertEqual(search_value, target, "No Value found against search term")


if __name__ == "__main__":
    unittest.main()
