import time
from pages.download_upload_page import *
from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
import unittest


class UploadDownload(unittest.TestCase):
    def test_download_upload(self):
        url = "https://demoqa.com/upload-download"
        load_func = UploadDownloadMethods(url)
        load_func.click(download_id)
        load_func.send_keys(upload_id, upload_path)
        text = load_func.get_text(upload_text)
        print(text)
        load_func.waiting(upload_text)
        clean_text = text.replace("C:\\fakepath\\", "")
        self.assertEqual(clean_text, file_name, "Test Failed")


if __name__ == "__main__":
    unittest.main()
