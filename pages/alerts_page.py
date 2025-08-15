from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class AlertsPage(BasePage):
    """
    Page object for the Alerts, Frame, & Windows page.
    """
    ALERT_BUTTON = (By.ID, "alertButton")
    TIMER_ALERT_BUTTON = (By.ID, "timerAlertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_alert_button(self):
        """Clicks the 'Click me to see an alert' button."""
        self.click(self.ALERT_BUTTON)

    def click_timer_alert_button(self):
        """Clicks the 'On button click, alert will appear after 5 seconds' button."""
        self.click(self.TIMER_ALERT_BUTTON)

    def click_confirm_button(self):
        """Clicks the 'On button click, confirm box will appear' button."""
        self.click(self.CONFIRM_BUTTON)

    def click_prompt_button(self):
        """Clicks the 'On button click, prompt box will appear' button."""
        self.click(self.PROMPT_BUTTON)

    def get_confirm_result(self) -> str:
        """Returns the text result after interacting with the confirm box."""
        return self.get_element_text(self.CONFIRM_RESULT)

    def get_prompt_result(self) -> str:
        """Returns the text result after interacting with the prompt box."""
        return self.get_element_text(self.PROMPT_RESULT)