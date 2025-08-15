from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    """
    Page Object Model for the Modal Dialogs page.
    This class encapsulates elements and logic for interacting with modal windows.
    """
    # Locators for elements
    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    LARGE_MODAL_BUTTON = (By.ID, "showLargeModal")

    # Locators for the small modal dialog
    SMALL_MODAL_TITLE = (By.ID, "example-modal-sizes-title-sm")
    SMALL_MODAL_BODY = (By.CLASS_NAME, "modal-body")
    SMALL_MODAL_CLOSE_BUTTON = (By.ID, "closeSmallModal")

    # Locators for the large modal dialog
    LARGE_MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    LARGE_MODAL_BODY = (By.CLASS_NAME, "modal-body")
    LARGE_MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")

    def __init__(self, driver):
        super().__init__(driver)

    def open_small_modal(self):
        """
        Clicks the button to open the small modal.
        """
        self.click(self.SMALL_MODAL_BUTTON)

    def open_large_modal(self):
        """
        Clicks the button to open the large modal.
        """
        self.click(self.LARGE_MODAL_BUTTON)

    def get_small_modal_content(self) -> dict:
        """
        Gets the title and body text from the small modal.
        Returns a dictionary with 'title' and 'body'.
        """
        return {
            "title": self.get_element_text(self.SMALL_MODAL_TITLE),
            "body": self.get_element_text(self.SMALL_MODAL_BODY)
        }

    def get_large_modal_content(self) -> dict:
        """
        Gets the title and body text from the large modal.
        Returns a dictionary with 'title' and 'body'.
        """
        return {
            "title": self.get_element_text(self.LARGE_MODAL_TITLE),
            "body": self.get_element_text(self.LARGE_MODAL_BODY)
        }

    def close_small_modal(self):
        """
        Closes the small modal by clicking its close button.
        """
        element = self.find_element(self.SMALL_MODAL_TITLE)
        self.click(self.SMALL_MODAL_CLOSE_BUTTON)
        self.wait.until(EC.staleness_of(element))

    def close_large_modal(self):
        """
        Closes the large modal by clicking its close button.
        """
        element = self.find_element(self.LARGE_MODAL_TITLE)
        self.click(self.LARGE_MODAL_CLOSE_BUTTON)
        self.wait.until(EC.staleness_of(element))

    def is_small_modal_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.SMALL_MODAL_TITLE))
            return True
        except TimeoutException:
            return False

    def is_large_modal_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.LARGE_MODAL_TITLE))
            return True
        except TimeoutException:
            return False
