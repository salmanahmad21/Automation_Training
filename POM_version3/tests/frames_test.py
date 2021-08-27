from pages.frames_page import *
import unittest


class Frames(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salmanahmad/Downloads/chromedriver")

    def test_frames(self):
        self.driver.get("https://demoqa.com/frames")
        obj = FramesMethods(self.driver)
        obj.switch_to_frame(frame1_id)
        frame1_text = obj.get_text(frame1_text_id)
        obj.switch_to_default()
        obj.switch_to_frame(frame2_id)
        frame2_text = obj.get_text(frame2_text_id)
        self.assertEqual(frame1_text, frame2_text, "Text of both frames are not matching")


if __name__ == "__main__":
    unittest.main()
