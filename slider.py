from os import wait
from selenium import webdriver
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")

driver.get("https://demoqa.com/slider")


slider_id = 'input[type="range"]'

slider_handle = driver.find_element_by_css_selector(slider_id)

action = ActionChains(driver)

action.drag_and_drop_by_offset(slider_handle, 150, 0)
action.perform()
