from pages.download_upload_page import *
import unittest


class DownloadUpload(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": "/Users/salmanahmad/Downloads/Selenium_Training"}
        options.add_experimental_option("prefs", preferences)
        print("Working")
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver",
                                       chrome_options=options)

    def test_download_upload(self):
        self.driver.get("https://demoqa.com/upload-download")
        obj = DownloadUploadMethods(self.driver)
        obj.click(download_id)
        obj.send_values(upload_id, upload_path)
        upload_text = obj.get_text(upload_get_text_id)
        obj.wait_for_ele_invisible(upload_get_text_id)
        upload_clean_text = obj.clean_text(upload_text, upload_file_name)
        self.assertEqual(upload_clean_text, upload_file_name, "file name not matched with uploaded file")


if __name__ == "__main__":
    unittest.main()
