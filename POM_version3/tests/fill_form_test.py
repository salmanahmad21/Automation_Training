from pages.fill_form_page import *
import unittest


class FillForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_fill_form(self):
        self.driver.get("https://demoqa.com/text-box")
        obj = FillFormMethods(self.driver)
        obj.form_fill(form_input_keys, form_input_values)
        obj.click(form_submit_btn_id)
        obj.output_result(output_text_ids)
        print(clean_values)
        self.assertEqual(form_input_values, clean_values, "Values are not matching - Failed")



if __name__ == "__main__":
    unittest.main()
