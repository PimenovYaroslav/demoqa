from selenium.webdriver.common.by import By
from .base_page import BasePage


class DatePickerPage(BasePage):
    """
    Page Object for the Date Picker page (DemoQA).
    This class encapsulates locators and methods specific to the date picker functionalities.
    """

    # Locators for both date pickers
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATETIME_INPUT = (By.ID, "dateAndTimePickerInput")

    # Locators for the standard date picker
    MONTH_DROPDOWN = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_DROPDOWN = (By.CLASS_NAME, "react-datepicker__year-select")
    DAY_CELL = "//div[contains(@class,'react-datepicker__day') " \
               "and not(contains(@class,'outside-month')) and text()='{day}']"

    # Locators for the DateTime picker (with custom UI)
    MONTH_READ_VIEW = (By.CLASS_NAME, "react-datepicker__month-read-view")
    YEAR_READ_VIEW = (By.CLASS_NAME, "react-datepicker__year-read-view")
    YEAR_OPTION = "//div[contains(@class,'react-datepicker__year-option') and text()='{year}']"
    MONTH_OPTION = "//div[contains(@class,'react-datepicker__month-option') and text()='{month}']"
    DAY_CELL_DT = "//div[contains(@class,'react-datepicker__day') and text()='{day}']"
    TIME_CELL = "//li[contains(@class,'react-datepicker__time-list-item') and text()='{time}']"

    def __init__(self, driver):
        super().__init__(driver)

    def select_date(self, day: str, month: str, year: str):
        """
        Selects a date in the standard date picker.

        Args:
            day (str): The day of the month to select.
            month (str): The month to select.
            year (str): The year to select.
        """
        self.click(self.DATE_INPUT)
        self.select_from_dropdown(self.MONTH_DROPDOWN, month, by_type="text")
        self.select_from_dropdown(self.YEAR_DROPDOWN, year, by_type="text")
        self.click((By.XPATH, self.DAY_CELL.format(day=day)))

    def select_date_time(self, day: str, month: str, year: str, time: str):
        """
        Selects a date and time in the custom DateTime picker.

        Args:
            day (str): The day of the month to select.
            month (str): The month to select.
            year (str): The year to select.
            time (str): The time to select.
        """
        self.wait_for_visibility_of_element(self.DATETIME_INPUT)
        self.js_click(self.DATETIME_INPUT)

        # Select the month from the dropdown
        self.js_click(self.MONTH_READ_VIEW)
        self.js_click((By.XPATH, self.MONTH_OPTION.format(month=month)))

        # Select the year from the dropdown
        self.js_click(self.YEAR_READ_VIEW)
        self.js_click((By.XPATH, self.YEAR_OPTION.format(year=year)))

        # Select the day
        self.js_click((By.XPATH, self.DAY_CELL_DT.format(day=day)))

        # Select the time
        self.js_click((By.XPATH, self.TIME_CELL.format(time=time)))

    def get_selected_date_value(self):
        """
        Retrieves the value of the standard date input field.
        """
        return self.get_element_value(self.DATE_INPUT)

    def get_selected_date_time_value(self):
        """
        Retrieves the value of the datetime input field.
        """
        return self.get_element_value(self.DATETIME_INPUT)
