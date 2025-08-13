from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RadioButtonPage(BasePage):
    """
    Page object model for the DemoQA Radio Button page.
    """
    # Locators for the radio buttons and result message
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    RESULT_MESSAGE = (By.CLASS_NAME, "mt-3")

    def __init__(self, driver):
        super().__init__(driver)

    def click_radio_button(self, button_name: str):
        """
        Clicks on a radio button based on its name.
        :param button_name: The name of the radio button ('Yes', 'Impressive', or 'No').
        """
        if button_name.lower() == 'yes':
            self.click(self.YES_RADIO_BUTTON)
        elif button_name.lower() == 'impressive':
            self.click(self.IMPRESSIVE_RADIO_BUTTON)
        elif button_name.lower() == 'no':
            # 'No' button is disabled, so we expect an error or it to be unclickable
            # We will handle this gracefully in our test.
            self.click(self.NO_RADIO_BUTTON)

    def get_result_message(self) -> str:
        """
        Retrieves the text from the result message displayed after a selection.
        :return: The text of the result message.
        """
        return self.get_element_text(self.RESULT_MESSAGE)

