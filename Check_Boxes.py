from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")

driver.get("https://demoqa.com/checkbox")

plus_btn = driver.find_element_by_css_selector(
    '[class="rct-icon rct-icon-expand-all"]')
plus_btn.click()
driver.implicitly_wait(5)
check_box = driver.find_element_by_css_selector('span.rct-checkbox')
check_box.click()
time.sleep(2)
check_box2 = driver.find_element_by_css_selector('span.rct-checkbox')
check_box2.click()
time.sleep(2)
collaps_btn = driver.find_element_by_css_selector(
    "button.rct-option-collapse-all")
collaps_btn.click()
