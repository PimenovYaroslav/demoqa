from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LinksPage(BasePage):
    """
    Page object model for the DemoQA Links page.
    """
    # Locators for the links
    HOME_LINK = (By.ID, "simpleLink")
    DYNAMIC_HOME_LINK = (By.ID, "dynamicLink")
    CREATED_LINK = (By.ID, "created")
    NO_CONTENT_LINK = (By.ID, "no-content")
    MOVED_LINK = (By.ID, "moved")
    BAD_REQUEST_LINK = (By.ID, "bad-request")
    UNAUTHORIZED_LINK = (By.ID, "unauthorized")
    FORBIDDEN_LINK = (By.ID, "forbidden")
    NOT_FOUND_LINK = (By.ID, "invalid-url")

    # Locator for the API response message
    LINK_RESPONSE_MESSAGE = (By.ID, "linkResponse")

    def __init__(self, driver):
        super().__init__(driver)

    def click_home_link(self):
        """
        Clicks the 'Home' link.
        """
        self.click(self.HOME_LINK)

    def click_dynamic_home_link(self):
        """
        Clicks the dynamic 'Home' link.
        """
        self.click(self.DYNAMIC_HOME_LINK)

    def click_created_link(self):
        """
        Clicks the 'Created' link.
        """
        self.click(self.CREATED_LINK)

    def click_no_content_link(self):
        """
        Clicks the 'No Content' link.
        """
        self.click(self.NO_CONTENT_LINK)

    def click_moved_link(self):
        """
        Clicks the 'Moved' link.
        """
        self.click(self.MOVED_LINK)

    def click_bad_request_link(self):
        """
        Clicks the 'Bad Request' link.
        """
        self.click(self.BAD_REQUEST_LINK)

    def click_unauthorized_link(self):
        """
        Clicks the 'Unauthorized' link.
        """
        self.click(self.UNAUTHORIZED_LINK)

    def click_forbidden_link(self):
        """
        Clicks the 'Forbidden' link.
        """
        self.click(self.FORBIDDEN_LINK)

    def click_not_found_link(self):
        """
        Clicks the 'Not Found' link.
        """
        self.click(self.NOT_FOUND_LINK)

    def get_link_message(self) -> str:
        """
        Retrieves the text from the link response message displayed after a link click.
        """
        return self.get_element_text(self.LINK_RESPONSE_MESSAGE)