from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re


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

output_text = [output_name_id, output_email_id, output_current_address_id, output_permanent_address_id]
get_output_data = []
clean_values = []


class FormMethods:
    def __init__(self, driver):
        self.driver = driver

    def clean_text(self, text):
        clean_text = re.sub('^(.*:)', "", text)
        return clean_text
