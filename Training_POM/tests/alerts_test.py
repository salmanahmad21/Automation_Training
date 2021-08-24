import time
from pages.download_upload_page import *
from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
from pages.alerts_page import *
import unittest


class Alerts(unittest.TestCase):
    def test_alerts(self):
        url = "https://demoqa.com/alerts"
        alert_func = AlertsMethods(url)
        alert_func.click(first_btn_id)
        alert_func.accept_wait_alerts()
        alert_func.click(second_btn_id)
        alert_func.waiting(get_result_text)
        alert_func.accept_wait_alerts()
        alert_func.click(third_btn_id)
        alert_func.dismiss_wait_alerts()
        text = alert_func.get_text(get_result_text)
        print(text)
        self.assertEqual(third_btn_expected_result, text,
                         "Clicked Text Not Matched - Failed")
        alert_func.click(forth_btn_id)
        alert_func.promt_wait_alerts(prompt_input_value)
        text = alert_func.get_text(prompt_result_text_id)
        clean_text = alert_func.clean_text(text, prompt_input_value)
        print(clean_text)
        self.assertEqual(clean_text, prompt_input_value,
                         "Text Not Match - Failed")
        alert_func.tearDown()


if __name__ == "__main__":
    unittest.main()
