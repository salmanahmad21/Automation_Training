import time

from selenium import webdriver
from pages.rows_page import *

import unittest


class RowsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_delete_row(self):
        self.driver.get("https://demoqa.com/webtables")
        obj = RowsMethods(self.driver)
        for i in range(len(ids)):
            obj.click(ids[i])
        remaining_ids = obj.get_all_elements(status_of_values)
        if not remaining_ids:
            status = False

        self.assertEqual(
            False, status, "IDs Not Deleted - Test Failed")

    def test_add_row(self):
        self.driver.get("https://demoqa.com/webtables")
        obj = RowsMethods(self.driver)
        obj.click(add_btn_id)
        for i in range(len(form_ids)):
            obj.send_values(form_ids[i], form_value[i])
        obj.click(submit_btn_id)
        total = obj.get_all_elements(total_records)
        print(len(total))
        self.assertGreater(len(total), 3, "Record Not Added - Failed")

    def test_search_row(self):
        self.driver.get("https://demoqa.com/webtables")
        obj = RowsMethods(self.driver)
        obj.send_values(search_box_id, search_value)
        result = obj.get_all_elements(find_record)
        obj.match_values(result)
        self.assertEqual(search_value, result, "Search value not matched")



if __name__ == "__main__":
    unittest.main()
