from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProgressBarPage(BasePage):
    """
    Page Object for the Progress Bar page (DemoQA).
    Provides methods to interact with the progress bar.
    """

    # Locators for the elements on the page
    START_STOP_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, "div[role='progressbar']")
    RESET_BUTTON = (By.ID, "resetButton")

    def __init__(self, driver):
        super().__init__(driver)

    def start_progress(self):
        """
        Clicks the 'Start' button to begin the progress bar.
        """
        self.click(self.START_STOP_BUTTON)

    def stop_progress(self):
        """
        Clicks the 'Stop' button to halt the progress bar.
        """
        self.click(self.START_STOP_BUTTON)

    def get_progress_value(self) -> int:
        """
        Returns the current progress value from the progress bar.
        Example: "75%" returns 75.
        """
        progress_text = self.find_element(self.PROGRESS_BAR).text
        return int(progress_text.strip('%'))

    def wait_for_completion(self, timeout: int = 20):
        """
        Explicitly waits for the progress bar to reach 100%.
        """
        self.wait_for_text_in_element(self.PROGRESS_BAR, "100%", timeout)

    def wait_for_value_to_exceed(self, threshold: int, timeout: int = 20):
        """
        Waits until the progress bar's value exceeds a given threshold.
        """
        self.wait_for_custom_condition(
            lambda d: self.get_progress_value() > threshold, timeout
        )

    def is_reset_button_visible(self) -> bool:
        """
        Checks if the 'Reset' button is visible on the page.
        """
        try:
            self.find_element(self.RESET_BUTTON)
            return True
        except Exception:
            return False

    def reset_progress(self):
        """
        Clicks the 'Reset' button to return the progress bar to 0%.
        """
        self.click(self.RESET_BUTTON)
