from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

pls_btn = (By.CLASS_NAME, "rct-icon-expand-all")
check_box = (By.CSS_SELECTOR, "span.rct-checkbox")
collap_btn = (By.CSS_SELECTOR, "button.rct-option-collapse-all")
all_result_text = ".display-result>span"
all_ele_text = []
expected_result = ['You have selected :', 'home', 'desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']




class CheckBoxesMethods:
    def __init__(self, driver):
        self.driver = driver




