from pages.base_page import *

tab_link_id = (By.ID, "simpleLink")
home_class = "home-body"


class SwitchMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def switch_tab(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def class_name_index(self, locator):
        return self.driver.find_elements_by_class_name(locator)[0].get_attribute('class')
