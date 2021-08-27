import time

from pages.alerts_page import *
import unittest


class Alerts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")


    def test_alerts(self):
        self.driver.get("https://demoqa.com/alerts")
        obj = AlertsMethods(self.driver)
        obj.click(first_btn_id)
        obj.accept_alerts()
        obj.click(second_btn_id)
        obj.accept_alerts()
        obj.click(third_btn_id)
        obj.dismiss_alerts()
        obj.click(forth_btn_id)
        obj.promt_alerts(prompt_input_value)
        third_btn_result_text = obj.get_text(third_btn_result_id)
        self.assertEqual(third_btn_expected_result, third_btn_result_text, "Clicks are not matching")
        forth_btn_text = obj.get_text(prompt_result_id)
        forth_btn_clean_text = obj.clean_text(forth_btn_text, prompt_input_value)
        self.assertEqual(forth_btn_clean_text, prompt_input_value, "Prompt text not matched")


if __name__ == "__main__":
    unittest.main()
