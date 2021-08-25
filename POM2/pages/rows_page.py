from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

add_btn_id = (By.ID, "addNewRecordButton")
status_of_values = "div[class='action-buttons'] span:nth-child(2)"
submit_btn_id = (By.ID, "submit")
first_name_id = (By.ID, "firstName")
last_name_id = (By.ID, "lastName")
email_id = (By.ID, "userEmail")
age_id = (By.ID, "age")
salary_id = (By.ID, "salary")
department_id = (By.ID, "department")
form_ids = [first_name_id, last_name_id, email_id, age_id, salary_id, department_id]
form_value = ["Salman", "Ahmad", "sulmanmansha@gmail.com", "27", "20000", "CsIT"]
delete_record_id1 = (By.ID, "delete-record-1")
delete_record_id2 = (By.ID, "delete-record-2")
delete_record_id3 = (By.ID, "delete-record-3")
ids = [delete_record_id1, delete_record_id2, delete_record_id3]
search_value = "39"
search_box_id = (By.ID, "searchBox")
find_record = "rt-td"
value = []
target = ""

total_records = ".action-buttons span:nth-child(2)"


class RowMethods:
    def __init__(self, driver):
        self.driver = driver










