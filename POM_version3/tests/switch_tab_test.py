from pages.switch_tab_page import *
import unittest


class SwitchTab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_switch_tab(self):
        self.driver.get("https://demoqa.com/links")
        obj = SwitchMethods(self.driver)
        obj.click(tab_link_id)
        switch_func = SwitchMethods(self.driver)
        switch_func.switch_tab()
        get_class_name = switch_func.class_name_index(home_class)
        print(get_class_name)
        self.assertEqual("home-body", get_class_name, "Home Class Not Found On New Page")


if __name__ == "__main__":
    unittest.main()
