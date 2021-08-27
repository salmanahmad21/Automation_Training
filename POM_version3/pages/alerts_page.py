from pages.base_page import *


prompt_input_value = "Salman"
first_btn_id = (By.ID, "alertButton")
second_btn_id = (By.ID, "timerAlertButton")
third_btn_id = (By.ID, "confirmButton")
forth_btn_id = (By.ID, "promtButton")
third_btn_result_id = (By.ID, "confirmResult")
prompt_result_id = (By.ID, "promptResult")
third_btn_expected_result = "You selected Cancel"



class AlertsMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def accept_alerts(self):
        try:
            WebDriverWait(self.driver, 8).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except (Exception, ValueError, TimeoutError, Exception):
            return None

    def dismiss_alerts(self):
        try:
            WebDriverWait(self.driver, 6).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except (Exception, ValueError, TimeoutError, Exception):
            return None

    def promt_alerts(self, keys):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.send_keys(keys)
            alert.accept()
        except (Exception, ValueError, TimeoutError, Exception):
            return None
