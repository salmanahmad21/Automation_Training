from pages.select_able_clicks_page import *
import unittest



class SelectAbleClicks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_select_able_clicks(self):
        self.driver.get("https://demoqa.com/selectable")
        obj = SelectAbleClicksMethods(self.driver)
        click_able = obj.get_all_elements(all_clickables_selector)
        unclicked_class_names = obj.get_before_click_class_name(click_able)
        clicked_class_names = obj.get_after_click_class_name(click_able, all_clickables_selector)
        self.assertNotEqual(unclicked_class_names, clicked_class_names, "Class names not changed - Failed")


if __name__ == "__main__":
    unittest.main()
