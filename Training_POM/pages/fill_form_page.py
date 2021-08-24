from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re


full_name_id ="userName"
full_name_input = "Salman Ahmad"
email_id = "userEmail"
email_input = "sulmanmansha123@gmail.com"
current_address_id = "currentAddress"
current_address_input = "78 B Muslim Nagar Raiwind Road Lahore"
permanent_address_id = "permanentAddress"
permanent_address_input = "78 B Muslim Nagar Raiwind Road Lahore"
submit_btn_id = "submit"
input_value = [full_name_id, email_id, current_address_id, permanent_address_id]
input_data = [full_name_input, email_input, current_address_input, permanent_address_input]

