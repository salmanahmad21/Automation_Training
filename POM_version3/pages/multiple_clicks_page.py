from pages.base_page import *


double_click_id = (By.ID, "doubleClickBtn")
right_click_id = (By.ID, "rightClickBtn")
simple_click = (By.CSS_SELECTOR, ".col-12.mt-4.col-md-6 .mt-4:nth-of-type(3)> button")

get_double_click_text = (By.ID, "doubleClickMessage")
get_right_click_text = (By.ID, "rightClickMessage")
get_dynamic_click_text = (By.ID, "dynamicClickMessage")



class MultipleClicksMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def double_click_actions(self, click_btn):
        action = ActionChains(self.driver)
        action.double_click(on_element=click_btn)
        action.perform()

    def right_click_actions(self, click_btn):
        action = ActionChains(self.driver)
        action.context_click(on_element=click_btn)
        action.perform()