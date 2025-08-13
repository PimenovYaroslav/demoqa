from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    """
    Page object model for the DemoQA Text Box page.
    This page is responsible for interacting with the form fields.
    """
    # Locators for the form fields and button
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    # Locators for the output section
    OUTPUT_FULL_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, full_name, email, current_address, permanent_address):
        """
        Fills out all fields in the text box form using the enhanced type_into_element method.
        :param full_name: The value for the Full Name field.
        :param email: The value for the Email field.
        :param current_address: The value for the Current Address field.
        :param permanent_address: The value for the Permanent Address field.
        """
        self.type_into_element(self.FULL_NAME_INPUT, full_name)
        self.type_into_element(self.EMAIL_INPUT, email)
        self.type_into_element(self.CURRENT_ADDRESS_INPUT, current_address)
        self.type_into_element(self.PERMANENT_ADDRESS_INPUT, permanent_address)

    def submit_form(self):
        """
        Clicks the submit button.
        """
        self.click(self.SUBMIT_BUTTON)

    def get_output_text(self):
        """
        Retrieves the output text after form submission.
        :return: A dictionary with the submitted data.
        """
        output = {
            "name": self.get_element_text(self.OUTPUT_FULL_NAME),
            "email": self.get_element_text(self.OUTPUT_EMAIL),
            "current_address": self.get_element_text(self.OUTPUT_CURRENT_ADDRESS),
            "permanent_address": self.get_element_text(self.OUTPUT_PERMANENT_ADDRESS)
        }
        return output
