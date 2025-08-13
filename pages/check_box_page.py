import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import List, Tuple


class CheckBoxPage(BasePage):
    """
    Page object model for the DemoQA Check Box page.
    """
    # Locators for the main elements on the CheckBox page
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    HOME_CHECKBOX_LABEL = (By.CSS_SELECTOR, "label[for='tree-node-home']")
    OUTPUT_SUCCESS_MESSAGE = (By.ID, "result")

    # Locator to find all checkbox titles (names)
    CHECKBOX_TITLES = (By.XPATH, "//span[@class='rct-title']")

    def __init__(self, driver):
        super().__init__(driver)

    def expand_all_folders(self):
        """
        Clicks the 'Expand All' button to show all nested checkboxes.
        """
        self.click(self.EXPAND_ALL_BUTTON)

    def click_home_checkbox(self):
        """
        Clicks the 'Home' checkbox label to select/deselect all checkboxes.
        """
        self.click(self.HOME_CHECKBOX_LABEL)

    def get_all_checkboxes_names(self) -> List[str]:
        """
        Gets a list of all checkbox names, excluding 'Home', in a cleaned format.
        :return: A list of strings with the names of all checkboxes.
        """
        names = []
        all_checkboxes = self.find_elements(self.CHECKBOX_TITLES)
        for checkbox in all_checkboxes:
            name = checkbox.text.strip().lower()
            if name != 'home':
                # Remove file extensions for consistent comparison
                if '.' in name:
                    name = name.split('.')[0]
                # Remove spaces to match the output format
                name = name.replace(' ', '')
                names.append(name)
        return names

    def get_selected_names_from_result(self) -> List[str]:
        """
        Parses the success message and returns a cleaned list of selected names.
        :return: A list of strings with the names of the selected items.
        """
        # Wait for the output message to appear
        output_text = self.get_element_text(self.OUTPUT_SUCCESS_MESSAGE)

        # Split the text into lines and remove the first line which says "You have selected :"
        selected_list = output_text.split('\n')[1:]

        # Clean and format each name for consistent comparison
        cleaned_names = []
        for name in selected_list:
            name = name.strip().lower().replace(' ', '')
            # The output includes 'home', but our comparison list doesn't, so we skip it.
            if name == 'home':
                continue
            cleaned_names.append(name)

        return cleaned_names

    def select_random_checkboxes_and_get_result(self) -> List[str]:
        """
        Selects a random checkbox and returns the names of all selected items
        from the result section.
        :return: A list of strings with the names of the selected items.
        """
        self.expand_all_folders()
        all_checkbox_titles = self.find_elements(self.CHECKBOX_TITLES)

        # Select a random checkbox, excluding 'Home'
        all_names = [title.text for title in all_checkbox_titles if title.text.lower() != 'home']
        if not all_names:
            return []

        random_name = random.choice(all_names)

        # Create a locator for the randomly selected checkbox and click it
        locator = (By.XPATH, f"//span[@class='rct-title' and text()='{random_name}']/..")
        self.click(locator)

        # Return the names that appear in the result box
        return self.get_selected_names_from_result()











