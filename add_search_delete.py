from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver import ActionChains
import unittest
import numpy as n


class Test(unittest.TestCase):

    def test_delete(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")

        driver.get("https://demoqa.com/webtables")
        save = []
        status = driver.find_elements_by_css_selector(
            "div[class='action-buttons'] span:nth-child(2)")
        for i in range(len(status)):
            save.append(status[i].get_attribute("id"))
        print(save)

        ids = ["delete-record-1", "delete-record-2", "delete-record-3"]

        for i in ids:
            delete_row = driver.find_element_by_id(i)
            delete_row.click()
            time.sleep(1)
        time.sleep(2)

        self.assertListEqual(
            ids, save, "Hence Deleted Ids are matches with stored Values   !!! Test Passed")
        driver.refresh()
        time.sleep(5)

        status_verify = driver.find_elements_by_css_selector(
            "div[class='action-buttons'] span:nth-child(2)")
        if len(status_verify) >= 1:
            print("Table has three rows")
        else:
            print("No rows found")
        driver.close()

    def test_add_row(self):
        driver = webdriver.Chrome(
            executable_path="/Users/salmanahmad/Downloads/chromedriver")

        driver.get("https://demoqa.com/webtables")
        time.sleep(3)
        old_status = driver.find_elements_by_css_selector(
            "div[class='action-buttons'] span:nth-child(2)")

        add_btn = driver.find_element_by_id("addNewRecordButton")
        add_btn.click()
        time.sleep(1)
        first_name = driver.find_element_by_id("firstName")
        first_name.send_keys("Salman")
        time.sleep(1)
        last_name = driver.find_element_by_id("lastName")
        last_name.send_keys("Ahmad")
        time.sleep(1)
        email = driver.find_element_by_id("userEmail")
        email.send_keys("sulman@gmail.com")
        time.sleep(1)
        age = driver.find_element_by_id("age")
        age.send_keys("26")
        time.sleep(1)
        salary = driver.find_element_by_id("salary")
        salary.send_keys("200000")
        time.sleep(1)
        department = driver.find_element_by_id("department")
        department.send_keys("IT")
        time.sleep(1)
        submit_btn = driver.find_element_by_id("submit")
        submit_btn.click()
        time.sleep(1)

        new_status = driver.find_elements_by_css_selector(
            "div[class='action-buttons'] span:nth-child(2)")
        if len(new_status) > len(old_status):
            print("Row Added")
        else:
            print("No Row Add")

        time.sleep(3)

        search_box = driver.find_element_by_id("searchBox")
        search_box.send_keys("Salman")
        time.sleep(5)

        result_list = driver.find_element_by_css_selector(
            "div.rt-tr-group .-odd").text
        compare = result_list.split()
        i = 0
        while i <= 5:
            if "Ahmad" == compare[i]:
                print("Final Result Matched")
                break
            else:
                print("Failed")
            i += 1


if __name__ == "__main__":
    unittest.main()
