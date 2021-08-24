import time

from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
import unittest


class Checkbox(unittest.TestCase):
    def test_clicks(self):
        url = "https://demoqa.com/buttons"

        func = DoubleClickMethod(url)
        double_click = func.click_by_id(double_click_id)
        action = ActionChains(func.driver)
        action.double_click(on_element=double_click)
        action.perform()
        right_click = func.click_by_id(right_click_id)
        action = ActionChains(func.driver)
        action.context_click(on_element=right_click)
        action.perform()
        func.click_by_css_selector(simple_click)



if __name__ == "__main__":
    unittest.main()
