from pages.multiple_clicks_page import *
import unittest


class MultipleClicks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_multiple_clicks(self):
        self.driver.get("https://demoqa.com/buttons")
        obj = MultipleClicksMethods(self.driver)
        d_click = obj.get_element_property(double_click_id)
        obj.double_click_actions(d_click)
        r_click = obj.get_element_property(right_click_id)
        obj.right_click_actions(r_click)
        obj.click(simple_click)
        d_click_text = obj.get_text(get_double_click_text)
        r_click_text = obj.get_text(get_right_click_text)
        dynamic_click_text = obj.get_text(get_dynamic_click_text)

        self.assertEqual("You have done a double click", d_click_text, "Double Click Text Not matched")
        self.assertEqual("You have done a right click", r_click_text, "Right Click Text Not matched")
        self.assertEqual("You have done a dynamic click", dynamic_click_text, "Dynamic Click Text Not matched")


if __name__ == "__main__":
    unittest.main()
