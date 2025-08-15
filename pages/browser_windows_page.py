from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    """
    A Page Object for the Browser Windows page on the DemoQA website.
    This class contains all the locators and methods for interacting with
    the elements on the Browser Windows page.
    """
    # Locators for the buttons on the Browser Windows page
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    NEW_WINDOW_MESSAGE_BUTTON = (By.ID, "messageWindowButton")

    # Locator for the text element that appears in the new tab/window
    NEW_WINDOW_TEXT = (By.XPATH, "//body")

    def __init__(self, driver):
        super().__init__(driver)

    def click_new_tab_button(self):
        """
        Clicks the 'New Tab' button to open a new tab.
        """
        self.click(self.NEW_TAB_BUTTON)

    def click_new_window_button(self):
        """
        Clicks the 'New Window' button to open a new browser window.
        """
        self.click(self.NEW_WINDOW_BUTTON)

    def click_new_window_message_button(self):
        """
        Clicks the 'New Window Message' button.
        """
        self.click(self.NEW_WINDOW_MESSAGE_BUTTON)

    def get_new_window_text(self):
        """
        Waits for the text on the new window to appear and returns it.
        This method uses a pre-defined locator to find the element and return its text.
        """
        return self.get_element_text(self.NEW_WINDOW_TEXT)





