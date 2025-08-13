from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ButtonsPage(BasePage):
    """
    Page object model for the DemoQA Buttons page.
    """
    # Locators for the buttons
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    # Locators for the success messages
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")

    def __init__(self, driver):
        super().__init__(driver)

    def double_click_on_button(self):
        """
        Performs a double click on the Double Click Me button.
        """
        button = self.find_element(self.DOUBLE_CLICK_BUTTON)
        ActionChains(self.driver).double_click(button).perform()

    def right_click_on_button(self):
        """
        Performs a right-click on the Right Click Me button.
        """
        button = self.find_element(self.RIGHT_CLICK_BUTTON)
        ActionChains(self.driver).context_click(button).perform()

    def click_on_button(self):
        """
        Performs a regular click on the Click Me button.
        """
        self.click(self.CLICK_ME_BUTTON)

    def get_double_click_message(self) -> str:
        """
        Retrieves the success message for the double click button.
        """
        return self.get_element_text(self.DOUBLE_CLICK_MESSAGE)

    def get_right_click_message(self) -> str:
        """
        Retrieves the success message for the right-click button.
        """
        return self.get_element_text(self.RIGHT_CLICK_MESSAGE)

    def get_dynamic_click_message(self) -> str:
        """
        Retrieves the success message for the dynamic click button.
        """
        return self.get_element_text(self.DYNAMIC_CLICK_MESSAGE)
