from pages.checkboxes_page import *
import unittest


class CheckBoxes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_checkboxes(self):
        self.driver.get("https://demoqa.com/checkbox")
        obj = CheckBoxesMethods(self.driver)
        obj.click(pls_btn)
        obj.click(check_box)
        obj.click(collap_btn)
        all_elements = obj.get_all_elements(all_result_text)
        element_text = obj.element_text(all_elements)
        self.assertEqual(expected_result, element_text, "Elements are not matching")


if __name__ == "__main__":
    unittest.main()
