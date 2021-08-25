from selenium import webdriver
from pages.base_page import *
from pages.fill_form_page import *
import unittest


class FillForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_fill_form(self):
        self.driver.get("https://demoqa.com/text-box")
        func = CommonMethods(self.driver)
        form_func = FormMethods(self.driver)
        for i in range(len(form_input_keys)):
            func.send_keys(form_input_keys[i], form_input_values[i])
        func.click(form_submit_btn_id)
        time.sleep(1)
        for i in range(len(output_text)):
            get_output_data.append(func.get_text(output_text[i]))
            clean_values.append(form_func.clean_text(get_output_data[i]))
        print(clean_values)
        self.assertEqual(form_input_values, clean_values, "Values are not matching - Failed")


if __name__ == "__main__":
    unittest.main()
