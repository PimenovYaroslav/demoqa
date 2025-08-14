from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import os
from typing import Tuple, List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage(BasePage):
    """
    Page Object for the Practice Form page, with methods to fill all fields.
    This class inherits from your provided BasePage.
    """

    # Locators for all form fields
    FIRST_NAME_INPUT: Tuple[str, str] = (By.ID, "firstName")
    LAST_NAME_INPUT: Tuple[str, str] = (By.ID, "lastName")
    EMAIL_INPUT: Tuple[str, str] = (By.ID, "userEmail")
    GENDER_MALE_RADIO: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE_RADIO: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER_RADIO: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_NUMBER_INPUT: Tuple[str, str] = (By.ID, "userNumber")
    DATE_OF_BIRTH_INPUT: Tuple[str, str] = (By.ID, "dateOfBirthInput")
    MONTH_SELECT: Tuple[str, str] = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_SELECT: Tuple[str, str] = (By.CLASS_NAME, "react-datepicker__year-select")
    SUBJECTS_INPUT: Tuple[str, str] = (By.ID, "subjectsInput")
    HOBBIES_SPORTS_CHECKBOX: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING_CHECKBOX: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC_CHECKBOX: Tuple[str, str] = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    PICTURE_UPLOAD: Tuple[str, str] = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_TEXTAREA: Tuple[str, str] = (By.ID, "currentAddress")
    STATE_CONTAINER: Tuple[str, str] = (By.ID, "stateCity-wrapper")
    STATE_DROPDOWN: Tuple[str, str] = (By.XPATH, "//div[@id='state']")
    CITY_DROPDOWN: Tuple[str, str] = (By.XPATH, "//div[@id='city']")
    STATE_INPUT: Tuple[str, str] = (By.ID, "react-select-3-input")
    CITY_INPUT: Tuple[str, str] = (By.ID, "react-select-4-input")
    SUBMIT_BUTTON: Tuple[str, str] = (By.ID, "submit")

    # Locators for the submission confirmation modal
    SUBMISSION_MODAL: Tuple[str, str] = (By.CSS_SELECTOR, ".modal-content")
    SUBMISSION_TABLE_ROWS: Tuple[str, str] = (By.XPATH, "//div[@class='modal-body']//tbody/tr")

    def __init__(self, driver):
        super().__init__(driver)

    def set_first_name(self, first_name: str):
        """Sets the value of the "First Name" field."""
        self.type_into_element(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name: str):
        """Sets the value of the "Last Name" field."""
        self.type_into_element(self.LAST_NAME_INPUT, last_name)

    def set_email(self, email: str):
        """Sets the value of the "Email" field."""
        self.type_into_element(self.EMAIL_INPUT, email)

    def set_gender(self, gender: str):
        """
        Selects the specified gender radio button.
        Args:
            gender: A string ("Male", "Female", or "Other").
        Raises:
            ValueError: If the provided gender is not supported.
        """
        gender_locators = {
            "Male": self.GENDER_MALE_RADIO,
            "Female": self.GENDER_FEMALE_RADIO,
            "Other": self.GENDER_OTHER_RADIO
        }

        if gender not in gender_locators:
            raise ValueError(f"Invalid gender: '{gender}'. Supported values are 'Male', 'Female', 'Other'.")

        self.click(gender_locators[gender])

    def set_mobile_number(self, mobile_number: str):
        """Sets the value of the "Mobile Number" field."""
        self.type_into_element(self.MOBILE_NUMBER_INPUT, mobile_number)

    def set_date_of_birth(self, day: str, month: str, year: str):
        """
        Selects the date of birth from the calendar widget.

        :param day: The day of the month as a string (e.g., "05").
        :param month: The month as a string (e.g., "January").
        :param year: The year as a string (e.g., "1990").
        """
        # Click the date of birth input to open the calendar widget
        self.click(self.DATE_OF_BIRTH_INPUT)

        # Use the universal select_from_dropdown method to select the year.
        # We use by_type="value" because the <select> tag for the year uses the 'value' attribute.
        self.select_from_dropdown(self.YEAR_SELECT, year, by_type="value")

        # Use the universal select_from_dropdown method to select the month.
        # We use by_type="text" because the <select> tag for the month uses the visible text.
        self.select_from_dropdown(self.MONTH_SELECT, month, by_type="text")

        # The logic for selecting the day remains as it is not related to a <select> tag.
        # We find the specific day element and click it to finalize the date selection.
        # The CSS selector is updated to handle both single and double-digit day formats.
        day_locator = (
            By.CSS_SELECTOR, f".react-datepicker__day--0{day.zfill(2)}:not(.react-datepicker__day--outside-month)")
        self.click(day_locator)

    def add_subjects(self, subjects: List[str]):
        """
        Types each subject into the input field and selects it from the dropdown.
        """
        subjects_element = self.find_element(self.SUBJECTS_INPUT)
        for subject in subjects:
            subjects_element.send_keys(subject)
            subjects_element.send_keys(Keys.ENTER)

    def set_hobbies(self, hobbies: List[str]):
        """
        Selects specified hobbies.
        Args:
            hobbies: A list of hobby names ("Sports", "Reading", "Music").
        """
        if "Sports" in hobbies:
            self.js_click(self.HOBBIES_SPORTS_CHECKBOX)
        if "Reading" in hobbies:
            self.js_click(self.HOBBIES_READING_CHECKBOX)
        if "Music" in hobbies:
            self.js_click(self.HOBBIES_MUSIC_CHECKBOX)

    def upload_picture(self, file_path: str):
        """
        Uploads a picture by providing the file path to the input element.
        """
        full_path = os.path.abspath(file_path)
        self.send_keys_to_hidden_element(self.PICTURE_UPLOAD, full_path)

    def set_current_address(self, address: str):
        """Sets the value of the "Current Address" textarea."""
        self.js_click(self.CURRENT_ADDRESS_TEXTAREA)
        self.type_into_element(self.CURRENT_ADDRESS_TEXTAREA, address)

    def set_state_and_city(self, state: str, city: str):
        """
        Selects a state and city from their respective dropdowns.
        Uses explicit waits and JS click to ensure stability.
        """
        # We will use the container element to click on, as it's more stable
        self.scroll_to_element(self.STATE_CONTAINER)

        # Click on the dropdown to open it. We don't click on the input directly.
        self.js_click(self.STATE_DROPDOWN)

        # Wait for the input field to be clickable after the dropdown is opened
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.STATE_INPUT)
        )
        self.type_into_element(self.STATE_INPUT, state, press_enter=True)

        self.js_click(self.CITY_DROPDOWN)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CITY_INPUT)
        )
        self.type_into_element(self.CITY_INPUT, city, press_enter=True)

    def submit_form(self):
        """Clicks the submit button."""
        self.click(self.SUBMIT_BUTTON)

    def verify_submission_data(self):
        """
        Verifies the data in the submission confirmation table.
        Returns: A dictionary of key-value pairs from the table.
        """
        self.find_element(self.SUBMISSION_MODAL)
        rows = self.find_elements(self.SUBMISSION_TABLE_ROWS)
        submission_data = {}
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) == 2:
                key = columns[0].text
                value = columns[1].text
                submission_data[key] = value
        return submission_data
