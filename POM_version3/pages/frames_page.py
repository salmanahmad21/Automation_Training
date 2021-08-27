from pages.base_page import *


frame1_id = "frame1"
frame2_id = "frame2"
frame1_text_id = (By.ID, "sampleHeading")
frame2_text_id = (By.ID, "sampleHeading")


class FramesMethods(BaseMethods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()
