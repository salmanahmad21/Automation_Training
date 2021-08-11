from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element_by_css_selector(
    '[id=userName]')
full_name.send_keys("Salman Ahmad")
email = driver.find_element_by_css_selector('[id = userEmail]')
email.send_keys("sulmanmansha123@gmail.com")
current_address = driver.find_element_by_css_selector("[id=currentAddress]")
current_address.send_keys("78 B Muslim Nagar Raiwind Road Lahore")
permanent_address = driver.find_element_by_css_selector(
    "[id=permanentAddress]")
permanent_address.send_keys("78 B Muslim Nagar Raiwind Road Lahore")
driver.implicitly_wait(5)
submit_btn = driver.find_element_by_css_selector("[id=submit]")
submit_btn.click()
