from pages.base_page import *
from pages.check_boxes_page import *
import unittest


class Checkbox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_check_boxes(self):
        self.driver.get("https://demoqa.com/checkbox")
        func = CommonMethods(self.driver)
        func.click(pls_btn)
        func.click(check_box)
        func.click(collap_btn)
        all_result_ele = func.get_len_all_elements(all_result_text)
        for i in range(len(all_result_ele)):
            all_ele_text.append(all_result_ele[i].text)
        print(all_ele_text)
        self.assertEqual(expected_result, all_ele_text, "Elements are not matching")


if __name__ == "__main__":
    unittest.main()