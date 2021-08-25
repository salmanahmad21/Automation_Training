from selenium import webdriver
from pages.rows_page import *
from pages.base_page import *

import unittest


class RowsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_add_row(self):
        self.driver.get("https://demoqa.com/webtables")
        func = CommonMethods(self.driver)
        func.click(add_btn_id)
        for i in range(len(form_ids)):
            func.send_keys(form_ids[i], form_value[i])
        func.click(submit_btn_id)
        total = func.get_len_all_elements(total_records)
        print(len(total))
        self.assertGreater(len(total), 3, "Record Not Added - Failed")

    def test_search_row(self):
        self.driver.get("https://demoqa.com/webtables")
        func = CommonMethods(self.driver)
        func.send_keys(search_box_id, search_value)
        result = func.get_len_all_elements(find_record)
        for i in range(len(result)):
            value.append(result[i].text)
        j = 0
        for j in range(len(value)):
            if value[j] == search_value:
                target = value[j]
                print("Value Matched in index")
        self.assertEqual(search_value, target, "No Value found against search term")

    def test_delete_row(self):
        self.driver.get("https://demoqa.com/webtables")
        func = CommonMethods(self.driver)
        for i in range(len(ids)):
            func.click(ids[i])
        time.sleep(3)
        remaining_ids = func.all_elements(status_of_values)
        if not remaining_ids:
            status = False

        self.assertEqual(
            False, status, "IDs Not Deleted - Test Failed")









if __name__ == "__main__":
    unittest.main()
