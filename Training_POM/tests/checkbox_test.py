from pages.row_page import *
from pages.checkboxes_page import *
import unittest


class Checkbox(unittest.TestCase):

    def test_check_boxes(self):
        url = "https://demoqa.com/checkbox"
        func = Methods(url)
        func.click_class_name(pls_btn)
        func.click_css_selector(check_box)
        func.click_css_selector(collap_btn)



if __name__ == "__main__":
    unittest.main()
