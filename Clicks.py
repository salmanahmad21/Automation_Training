from os import wait
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")

driver.get("https://demoqa.com/buttons")

double_click = driver.find_element_by_id('doubleClickBtn')
action = ActionChains(driver)
action.double_click(on_element=double_click)
action.perform()

time.sleep(1)
right_click = driver.find_element_by_id("rightClickBtn")
action.context_click(on_element=right_click)
action.perform()


time.sleep(1)
driver.find_element_by_css_selector(
    ".col-12.mt-4.col-md-6 .mt-4:nth-of-type(3)> button").click()
