from pages.base_page import *

upload_file_name = "leo_astrology_sign.jpeg"
download_id = (By.ID, "downloadButton")
upload_id = (By.ID, "uploadFile")
upload_path = "/Users/salmanahmad/Downloads/Selenium_Training/leo_astrology_sign.jpeg"
upload_get_text_id = (By.ID, "uploadedFilePath")


class DownloadUploadMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
