from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re

first_frame_id = "frame1"
second_frame_id = "frame2"
frame1_text_id = "sampleHeading"
frame2_text_id = frame1_text_id

get_frame_text = (By.ID, frame1_text_id)



