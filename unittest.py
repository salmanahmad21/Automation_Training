from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import unittest
import re
from selenium.webdriver import ActionChains


class Test(unittest.TestCase):

    def test_radio_button(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")
        driver.get("https://demoqa.com/radio-button")
        time.sleep(2)
        yes_click = "document.querySelector('input[id=yesRadio]').click()"
        driver.execute_script(yes_click)
        time.sleep(3)
        yes_click_result = driver.find_element_by_xpath(
            "//div/p[@class='mt-3']/span").text
        time.sleep(2)
        impressive_click = "document.querySelector('input[id=impressiveRadio]').click()"
        driver.execute_script(impressive_click)
        time.sleep(2)
        impressive_click_result = driver.find_element_by_xpath(
            "//div/p[@class='mt-3']/span").text
        time.sleep(2)

        self.assertEqual("Yes", yes_click_result, "Test Failed")
        self.assertEqual("Impressive", impressive_click_result, "Test Failed")

    def test_form(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")

        driver.get("https://demoqa.com/text-box")
        input_name = "Salman"
        input_email = "sulmanmansha@gmail.com"
        input_current_address = "78 B Muslim Nagar Adda Plot Jati Umra Raiwind Road Lahore"
        input_permanent_address = "78 B Muslim Nagar Adda Plot Jati Umra Raiwind Road Lahore"
        full_name = driver.find_element_by_css_selector(
            '[id=userName]')
        full_name.send_keys(f'{input_name}')
        print(full_name)

        time.sleep(1)
        email = driver.find_element_by_css_selector('[id = userEmail]')
        email.send_keys(f'{input_email}')
        time.sleep(1)
        current_address = driver.find_element_by_css_selector(
            "[id=currentAddress]")
        current_address.send_keys(f'{input_current_address}')
        permanent_address = driver.find_element_by_css_selector(
            "[id=permanentAddress]")
        permanent_address.send_keys(f'{input_permanent_address}')
        driver.implicitly_wait(5)

        submit_btn = driver.find_element_by_css_selector("[id=submit]")
        time.sleep(1)
        submit_btn.click()
        time.sleep(1)
        get_name = driver.find_element_by_css_selector(
            ".col-sm-12>p[id=name]").text
        get_email = driver.find_element_by_css_selector(
            ".col-sm-12>p[id=email]").text
        get_currnet_address = driver.find_element_by_css_selector(
            ".col-sm-12>p[id=currentAddress]").text
        get_permanent_address = driver.find_element_by_css_selector(
            ".col-sm-12>p[id=permanentAddress]").text
        time.sleep(1)

        clean_name = re.sub('^(.*:)', "", get_name)
        clean_email = re.sub('^(.*:)', "", get_email)
        clean_caddress = re.sub('^(.*:)', "", get_currnet_address)
        clean_paddress = re.sub('^(.*:)', "", get_permanent_address)

        print(clean_name, clean_email)
        self.assertEqual(input_name, clean_name, "Name Not Match")
        self.assertEqual(input_email,
                         clean_email, "Email Not Match")
        self.assertEqual(input_current_address, clean_caddress,
                         "current address Not Match")
        self.assertEqual(input_permanent_address, clean_paddress,
                         "permanent address Not Match")

        time.sleep(1)

    def test_clicks(self):
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

        dynamic_click = driver.find_element_by_css_selector(
            ".col-12.mt-4.col-md-6 .mt-4:nth-of-type(3)> button").click()
        time.sleep(1)
        double_click_text = driver.find_element_by_css_selector(
            "p[id=doubleClickMessage]").text

        right_click_text = driver.find_element_by_css_selector(
            "p[id='rightClickMessage']").text

        dynamic_click_text = driver.find_element_by_css_selector(
            "p[id='dynamicClickMessage']").text
        print(double_click_text)
        print(right_click_text)
        print(dynamic_click_text)
        time.sleep(1)
        self.assertEqual("You have done a double click",
                         double_click_text, "double click test not matched")
        self.assertEqual("You have done a right click",
                         right_click_text, "right click test not matched")
        self.assertEqual("You have done a dynamic click",
                         dynamic_click_text, "Dynamic click test not matched")

    def test_checkboxes(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")

        driver.get("https://demoqa.com/checkbox")

        plus_btn = driver.find_element_by_css_selector(
            '[class="rct-icon rct-icon-expand-all"]')
        plus_btn.click()
        driver.implicitly_wait(5)
        check_box = driver.find_element_by_css_selector('span.rct-checkbox')
        check_box.click()
        result_text = driver.find_element_by_css_selector(
            "[id='result']>span").text
        print(result_text)
        time.sleep(2)
        check_box2 = driver.find_element_by_css_selector('span.rct-checkbox')
        check_box2.click()
        time.sleep(2)

        collaps_btn = driver.find_element_by_css_selector(
            "button.rct-option-collapse-all")
        collaps_btn.click()
        self.assertEqual("You have selected :", result_text, "Test Failed")

    def test_upload(self):
        file_name = "leo_astrology_sign.jpeg"
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": "/Users/salmanahmad/Downloads/Selenium_Training"}
        options.add_experimental_option("prefs", preferences)

        # Lunch Browser
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver", chrome_options=options)

        driver.get("https://demoqa.com/upload-download")

        # Download File
        download = driver.find_element_by_css_selector(
            "[id=downloadButton]")
        download.click()

        # Upload File

        upload = driver.find_element_by_css_selector(
            "input[id=uploadFile]")
        upload.send_keys(
            f"/Users/salmanahmad/Downloads/Selenium_Training/leo_astrology_sign.jpeg")

        upload_result = driver.find_element_by_css_selector(
            "p[id='uploadedFilePath']").text

        clean_text = upload_result.replace("C:\\fakepath\\", "")
        self.assertEqual(clean_text, file_name, "Test Failed")

        print(clean_text)


if __name__ == "__main__":
    unittest.main()
