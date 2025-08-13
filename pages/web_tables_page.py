from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WebTablesPage(BasePage):
    """
    Page object model for the DemoQA Web Tables page.
    """
    # Locators for the table elements
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SEARCH_BOX = (By.ID, "searchBox")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")

    # Locators for the registration form
    REGISTRATION_FORM = (By.ID, "registration-form-modal")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")

    # Dynamic locators for edit and delete buttons
    # We use a template to find a button in a specific row.
    EDIT_BUTTON_TEMPLATE = (By.XPATH, "//*[@class='rt-tr-group'][.//*[text()='{}']]//*[@title='Edit']")
    DELETE_BUTTON_TEMPLATE = (By.XPATH, "//*[@class='rt-tr-group'][.//*[text()='{}']]//*[@title='Delete']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_button(self):
        """
        Clicks the 'Add' button to open the registration form.
        """
        self.click(self.ADD_BUTTON)

    def fill_and_submit_form(self, first_name, last_name, email, age, salary, department):
        """
        Fills out the registration form and clicks submit.
        """
        self.type_into_element(self.FIRST_NAME_INPUT, first_name)
        self.type_into_element(self.LAST_NAME_INPUT, last_name)
        self.type_into_element(self.EMAIL_INPUT, email)
        self.type_into_element(self.AGE_INPUT, age)
        self.type_into_element(self.SALARY_INPUT, salary)
        self.type_into_element(self.DEPARTMENT_INPUT, department)
        self.click(self.SUBMIT_BUTTON)

    def edit_record(self, record_to_find, new_first_name):
        """
        Finds a record by name and edits the 'First Name' field.
        :param record_to_find: The unique identifier to find the record (e.g., 'Cierra').
        :param new_first_name: The new first name to enter.
        """
        edit_button_locator = (self.EDIT_BUTTON_TEMPLATE[0], self.EDIT_BUTTON_TEMPLATE[1].format(record_to_find))
        self.click(edit_button_locator)
        self.type_into_element(self.FIRST_NAME_INPUT, new_first_name)
        self.click(self.SUBMIT_BUTTON)

    def delete_record(self, record_to_find):
        """
        Finds a record by name and clicks the delete button.
        :param record_to_find: The unique identifier to find the record (e.g., 'Cierra').
        """
        delete_button_locator = (self.DELETE_BUTTON_TEMPLATE[0], self.DELETE_BUTTON_TEMPLATE[1].format(record_to_find))
        self.click(delete_button_locator)

    def get_table_data(self) -> list[dict]:
        """
        Retrieves all data from the table and returns it as a list of dictionaries.
        """
        table_data = []
        rows = self.find_elements(self.TABLE_ROWS)
        for row in rows:
            # Get the cells for the current row
            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
            if len(cells) > 0 and cells[0].text:  # Avoid empty rows
                table_data.append({
                    "first_name": cells[0].text,
                    "last_name": cells[1].text,
                    "age": cells[2].text,
                    "email": cells[3].text,
                    "salary": cells[4].text,
                    "department": cells[5].text
                })
        return table_data

