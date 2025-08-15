from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class FramesPage(BasePage):
    """
    Page object for the Frames page.
    """
    FRAME1_ID = "frame1"
    FRAME2_ID = "frame2"

    # Common locator for the heading text inside the frames
    FRAME_HEADING = (By.ID, "sampleHeading")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_text_from_frame(self, frame_id: str) -> str:
        """
        Switches to a specified frame, gets the text from the heading,
        and switches back to the default content.
        """
        # Switch to the frame using its ID
        self.driver.switch_to.frame(frame_id)

        # Get the text from the element inside the frame
        heading_text = self.get_element_text(self.FRAME_HEADING)

        # Switch back to the main document
        self.driver.switch_to.default_content()

        return heading_text
