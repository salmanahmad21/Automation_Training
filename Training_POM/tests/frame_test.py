import time
from pages.download_upload_page import *
from pages.row_page import *
from pages.checkboxes_page import *
from pages.doubleClick_page import *
from pages.alerts_page import *
from pages.select_able_click_page import *
from pages.frames_page import *
import unittest


class Iframes(unittest.TestCase):
    def test_iframes(self):
        url = "https://demoqa.com/frames"
        func = Methods(url)
        func.switch_to_frame(first_frame_id)
        frame1_text = func.get_text(get_frame_text)
        print(frame1_text)
        func.switch_to_default()
        func.switch_to_frame(second_frame_id)
        frame2_text = func.get_text(get_frame_text)
        print(frame2_text)
        self.assertEqual(frame1_text, frame2_text, "Text Are Not Same In Both Frames")


if __name__ == "__main__":
    unittest.main()
