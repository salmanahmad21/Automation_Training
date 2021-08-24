import time
from pages.download_upload_page import *
from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
from pages.fill_form_page import *
import unittest


class FillForm(unittest.TestCase):
    def test_fill_form(self):
        url = "https://demoqa.com/text-box"
        func = Methods(url)
        for i in range(len(input_data)):
            func.send_keys(input_value[i], input_data[i])
        func.click(submit_btn_id)


if __name__ == "__main__":
    unittest.main()
