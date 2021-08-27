from pages.base_page import *


all_clickables_selector = "#verticalListContainer>li"


class SelectAbleClicksMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def get_before_click_class_name(self, click_able):
        obj = SelectAbleClicksMethods(self.driver)
        all_class_names = []
        for i in range(len(click_able)):
            all_class_names.append(click_able[i].get_attribute("class"))
        return all_class_names


    def get_after_click_class_name(self, click_able, locator):
        obj = SelectAbleClicksMethods(self.driver)
        clicked_class_names = []
        for i in range(len(click_able)):
            self.driver.find_elements_by_css_selector(locator)[i].click()
            clicked_class_names.append(click_able[i].get_attribute("class"))
        return clicked_class_names

