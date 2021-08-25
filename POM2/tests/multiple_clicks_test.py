import unittest
from pages.multiple_clicks_page import *
from pages.base_page import *



class MultipleClicks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_multiple_clicks(self):
        self.driver.get("https://demoqa.com/buttons")
        func = CommonMethods(self.driver)
        click_func = MutlipleClicksMethods(self.driver)
        d_click = func.click_return(double_click_id)
        click_func.Double_click_actions(d_click)
        r_click = func.click_return(right_click_id)
        click_func.Right_click_actions(r_click)
        func.click(simple_click)
        d_click_text = func.get_text(get_double_click_text)
        r_click_text = func.get_text(get_right_click_text)
        dynamic_click_text = func.get_text(get_dynamic_click_text)

        self.assertEqual("You have done a double click", d_click_text, "Double Click Text Not matched")
        self.assertEqual("You have done a right click", r_click_text, "Right Click Text Not matched")
        self.assertEqual("You have done a dynamic click", dynamic_click_text, "Dynamic Click Text Not matched")


if __name__ == "__main__":
    unittest.main()

