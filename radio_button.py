from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")

driver.get("https://demoqa.com/radio-button")

time.sleep(2)
javaScript = "document.querySelector('input[id=yesRadio]').click()"
driver.execute_script(javaScript)


time.sleep(2)
javaScript = "document.querySelector('.col-md-6 .custom-control:nth-of-type(3) input').click()"
driver.execute_script(javaScript)
