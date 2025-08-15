from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    """
    Page Object Model for the Nested Frames page.
    This class encapsulates elements and logic for interacting with iframes.
    """
    # Constant data for the page
    PARENT_FRAME_ID = "frame1"

    # Locators for elements within the iframes
    CHILD_IFRAME_LOCATOR = (By.TAG_NAME, "iframe") # Locator for the nested iframe element
    PARENT_HEADING = (By.TAG_NAME, "body")  # The text "Parent frame" is in the <body> tag
    CHILD_HEADING = (By.TAG_NAME, "p")  # The text "Child Iframe" is in the <p> tag

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_text_from_parent_frame(self) -> str:
        """
        Switches to the parent frame, gets the text, and returns to the main content.
        """
        try:
            # Switch to the parent frame by its ID
            self.driver.switch_to.frame(self.PARENT_FRAME_ID)

            # Find the element and get its text
            parent_text = self.get_element_text(self.PARENT_HEADING)

            # Crucially, return to the main content to access other frames
            self.driver.switch_to.default_content()

            return parent_text
        except NoSuchElementException:
            self.driver.switch_to.default_content()
            return "Parent frame not found."

    def get_text_from_child_frame(self) -> str:
        """
        Switches to the parent frame, then to the child frame, gets the text,
        and returns to the main content.
        """
        try:
            # Step 1: First, switch to the parent frame
            self.driver.switch_to.frame(self.PARENT_FRAME_ID)

            # Step 2: Now, inside the parent frame, find the child iframe element.
            child_iframe_element = self.driver.find_element(*self.CHILD_IFRAME_LOCATOR)

            # Step 3: Switch to the child iframe using the located WebElement
            self.driver.switch_to.frame(child_iframe_element)

            # Step 4: Find the element with the desired text and get the text
            child_text = self.driver.find_element(*self.CHILD_HEADING).text

            # Step 5: Return to the parent frame first, then to the main content.
            # This is important to not remain "inside" the frame.
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.default_content()

            return child_text
        except NoSuchElementException:
            self.driver.switch_to.default_content()
            return "Child frame not found."
