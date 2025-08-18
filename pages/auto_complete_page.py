from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    """
    Page object model for the DemoQA Auto Complete page.
    Includes refactored locators and improved synchronization.
    """
    # Locators
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "#autoCompleteSingleContainer input")
    SINGLE_COLOR_VALUE_DISPLAY = (By.CSS_SELECTOR, "div.auto-complete__single-value")
    MULTIPLE_COLORS_INPUT = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer input")
    SELECT_OPTIONS = (By.CSS_SELECTOR, "div.auto-complete__option")
    MULTI_SELECTED_VALUES = (By.CSS_SELECTOR, "div.auto-complete__multi-value__label")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "div.auto-complete__multi-value__remove")

    def __init__(self, driver):
        super().__init__(driver)

    # Actions
    def enter_multi_value(self, text: str, press_enter=True):
        """
        Enters a value into the multiple-color input field and optionally
        presses Enter.
        """
        self.type_into_element(self.MULTIPLE_COLORS_INPUT, text, press_enter)

    def enter_single_value(self, text: str, press_enter=True):
        """
        Enters a value into the single-color input field and optionally
        presses Enter.
        """
        self.wait_for_visibility_of_element(self.SINGLE_COLOR_INPUT, 5)
        self.type_into_element(self.SINGLE_COLOR_INPUT, text, press_enter)

    def get_suggestions(self):
        """
        Retrieves the text of all available suggestions in the dropdown.
        """
        return [el.text for el in self.find_elements(self.SELECT_OPTIONS)]

    def get_selected_multi_values(self):
        """
        Retrieves the text of all selected colors in the multiple-color field.
        """
        return [el.text for el in self.find_elements(self.MULTI_SELECTED_VALUES)]

    def is_single_value_selected(self, value: str):
        """
        Checks if the single auto-complete field has the specified value selected.
        This method contains the dynamic locator logic.
        """
        locator = (By.XPATH, f"//div[contains(@class, 'single-value') and text()='{value}']")
        return self.is_element_visible(locator)

    def remove_last_multi_value(self):
        """
        Clicks the remove button for the last selected color.
        """
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if buttons:
            buttons[-1].click()
