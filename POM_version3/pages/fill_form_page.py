from pages.base_page import *

input_name = "Salman"
input_email = "sulmanmansha@gmail.com"
input_current_address = "78 B Muslim Nagar Adda Plot Jati Umra Raiwind Road Lahore"
input_permanent_address = "78 B Muslim Nagar Adda Plot Jati Umra Raiwind Road Lahore"
form_input_values = [input_name, input_email, input_current_address, input_permanent_address]
form_name_id = (By.ID, "userName")
form_email_id = (By.ID, "userEmail")
form_current_address_id = (By.ID, "currentAddress")
form_permanent_address_id = (By.ID, "permanentAddress")
form_submit_btn_id = (By.ID, "submit")
form_input_keys = [form_name_id, form_email_id, form_current_address_id, form_permanent_address_id]

output_name_id = (By.ID, "name")
output_email_id = (By.ID, "email")
output_current_address_id = (By.CSS_SELECTOR, ".border [id='currentAddress']")
output_permanent_address_id = (By.CSS_SELECTOR, ".border [id='permanentAddress']")

output_text_ids = [output_name_id, output_email_id, output_current_address_id, output_permanent_address_id]
get_output_data = []
clean_values = []


class FillFormMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def clean_text(self, text):
        clean_text = re.sub('^(.*:)', "", text)
        return clean_text

    def form_fill(self, form_input_keys, form_input_values):
        obj = FillFormMethods(self.driver)
        for i in range(len(form_input_keys)):
            obj.send_values(form_input_keys[i], form_input_values[i])

    def output_result(self, output_text_ids):
        obj = FillFormMethods(self.driver)
        for i in range(len(output_text_ids)):
            get_output_data.append(obj.get_text(output_text_ids[i]))
            clean_values.append(obj.clean_text(get_output_data[i]))















