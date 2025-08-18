from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class AccordionPage(BasePage):
    """
    Page Object Model for the Accordion page.
    This class inherits from BasePage and handles all interactions with
    accordion elements, using the generic methods provided by the parent class.
    """

    # Locators for the accordion sections
    SECTION_1_HEADING = (By.ID, "section1Heading")
    SECTION_1_CONTENT = (By.ID, "section1Content")

    SECTION_2_HEADING = (By.ID, "section2Heading")
    SECTION_2_CONTENT = (By.ID, "section2Content")

    SECTION_3_HEADING = (By.ID, "section3Heading")
    SECTION_3_CONTENT = (By.ID, "section3Content")

    def __init__(self, driver):
        super().__init__(driver)

    def open_section_1(self):
        """Clicks the heading of the first accordion section."""
        self.click(self.SECTION_1_HEADING)

    def is_section_1_expanded(self) -> bool:
        """Checks if the content of the first section is visible."""
        return self.is_element_visible(self.SECTION_1_CONTENT)

    def is_section_1_collapsed(self) -> bool:
        """Checks if the content of the first section is invisible (collapsed)."""
        return self.wait_for_invisibility(self.SECTION_1_CONTENT)

    def get_section_1_content(self) -> str:
        """Returns the text content of the first section."""
        return self.get_element_text(self.SECTION_1_CONTENT)

    def open_section_2(self):
        """Clicks the heading of the second accordion section."""
        self.click(self.SECTION_2_HEADING)

    def is_section_2_expanded(self) -> bool:
        """Checks if the content of the second section is visible."""
        return self.is_element_visible(self.SECTION_2_CONTENT)

    def is_section_2_collapsed(self) -> bool:
        """Checks if the content of the second section is invisible (collapsed)."""
        return self.wait_for_invisibility(self.SECTION_2_CONTENT)

    def get_section_2_content(self) -> str:
        """Returns the text content of the second section."""
        return self.get_element_text(self.SECTION_2_CONTENT)

    def open_section_3(self):
        """Clicks the heading of the third accordion section."""
        self.click(self.SECTION_3_HEADING)

    def is_section_3_expanded(self) -> bool:
        """Checks if the content of the third section is visible."""
        return self.is_element_visible(self.SECTION_3_CONTENT)

    def is_section_3_collapsed(self) -> bool:
        """Checks if the content of the third section is invisible (collapsed)."""
        return self.wait_for_invisibility(self.SECTION_3_CONTENT)

    def get_section_3_content(self) -> str:
        """Returns the text content of the third section."""
        return self.get_element_text(self.SECTION_3_CONTENT)
