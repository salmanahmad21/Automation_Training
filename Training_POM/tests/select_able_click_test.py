import time
from pages.download_upload_page import *
from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
from pages.alerts_page import *
from pages.select_able_click_page import *
import unittest


class SelectAbleClick(unittest.TestCase):
    def test_select_able_click(self):
        url = "https://demoqa.com/selectable"
        click_func = ClickAblesMethod(url)
        click_able = click_func.total_click_able(get_total_clickAbles)
        class_name = click_func.get_all_class_name(click_able)
        after_click_class_names = click_func.after_click_class_name(click_able)
        print(class_name)
        print(after_click_class_names)
        self.assertNotEqual(class_name,after_click_class_names, "Class Names Not Changed - Test Failed")

if __name__ == "__main__":
    unittest.main()
