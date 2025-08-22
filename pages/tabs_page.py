from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TabsPage(BasePage):
    """
    Page Object Model for the Tabs page on the DemoQA website.
    """

    # Locators declared as constants at the beginning of the class
    WHAT_TAB = (By.ID, "demo-tab-what")
    ORIGIN_TAB = (By.ID, "demo-tab-origin")
    USE_TAB = (By.ID, "demo-tab-use")

    # Locators for the content of each tab
    WHAT_TAB_CONTENT = (By.ID, "demo-tabpane-what")
    ORIGIN_TAB_CONTENT = (By.ID, "demo-tabpane-origin")
    USE_TAB_CONTENT = (By.ID, "demo-tabpane-use")

    def __init__(self, driver):
        super().__init__(driver)

    def click_what_tab(self):
        """
        Clicks the 'What' tab.
        """
        self.click(self.WHAT_TAB)

    def click_origin_tab(self):
        """
        Clicks the 'Origin' tab.
        """
        self.click(self.ORIGIN_TAB)

    def click_use_tab(self):
        """
        Clicks the 'Use' tab.
        """
        self.click(self.USE_TAB)

    def get_what_tab_content_text(self):
        """
        Returns the text content of the 'What' tab.
        """
        return self.get_element_text(self.WHAT_TAB_CONTENT)

    def get_origin_tab_content_text(self):
        """
        Returns the text content of the 'Origin' tab.
        """
        return self.get_element_text(self.ORIGIN_TAB_CONTENT)

    def get_use_tab_content_text(self):
        """
        Returns the text content of the 'Use' tab.
        """

        return self.get_element_text(self.USE_TAB_CONTENT)
