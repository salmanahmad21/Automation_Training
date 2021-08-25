from selenium import webdriver
from pages.rows_page import *
from pages.base_page import *
from pages.swtich_urls_page import *

import unittest


class SwitchUrls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")


    def test_switch_urls(self):
        self.driver.get("https://demoqa.com/links")
        func = CommonMethods(self.driver)
        func.click(tab_link_id)
        switch_func = SwitchMethods(self.driver)
        switch_func.switch_tabe()
        get_class_name = switch_func.class_name_index(home_class)
        print(get_class_name)
        self.assertEqual("home-body", get_class_name, "Home Class Not Found On New Page")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
