from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DynamicPropertiesPage(BasePage):
    """
    Page object model for the Dynamic Properties page.
    """
    # Locators for elements on the page
    TEXT_WITH_RANDOM_ID = (By.XPATH, "//p[text()='This text has random Id']")
    ENABLE_BUTTON_AFTER_FIVE_SECONDS = (By.ID, "enableAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_BUTTON = (By.ID, "visibleAfter")

    def __init__(self, driver):
        super().__init__(driver)

    def is_text_with_random_id_displayed(self) -> bool:
        """
        Checks if the static text element with a random ID is displayed using the
        reusable method from the BasePage.
        :return: True if the element is displayed, False otherwise.
        """
        return self.is_element_visible(self.TEXT_WITH_RANDOM_ID)

    def check_enable_button(self, timeout: int = 6) -> bool:
        """
        Waits for the 'Enable after 5 seconds' button to become clickable and returns its status.
        :param timeout: Maximum time to wait in seconds.
        :return: True if the button becomes clickable, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.ENABLE_BUTTON_AFTER_FIVE_SECONDS)
            )
            return True
        except TimeoutException:
            return False

    def check_color_change(self, timeout: int = 6) -> bool:
        """
        Waits for the color of the 'Color Change' button to change to red.
        :param timeout: Maximum time to wait in seconds.
        :return: True if the color changes to red, False otherwise.
        """
        # The button's class changes to 'text-danger' which corresponds to red
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.text-danger"))
            )
            return True
        except TimeoutException:
            return False

    def check_visible_after_button(self, timeout: int = 6) -> bool:
        """
        Waits for the 'Visible after 5 seconds' button to become visible.
        :param timeout: Maximum time to wait in seconds.
        :return: True if the button becomes visible, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.VISIBLE_AFTER_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def get_button_color(self) -> str:
        """
        Gets the CSS color value of the color change button.
        :return: The color value as a string (e.g., 'rgba(220, 53, 69, 1)').
        """
        button_element = self.driver.find_element(*self.COLOR_CHANGE_BUTTON)
        return button_element.value_of_css_property('color')