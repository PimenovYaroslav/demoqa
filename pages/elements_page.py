from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    """
    Page object model for the DemoQA Elements page.
    This page is responsible for the left-side menu and its navigation.
    """
    # Locators for the left-side menu items
    HEADER = (By.XPATH, "//div[@class='header-text' and text()='Elements']")
    TEXT_BOX_ITEM = (By.XPATH, "//span[text()='Text Box']")
    CHECK_BOX_ITEM = (By.XPATH, "//span[text()='Check Box']")
    RADIO_BUTTON_ITEM = (By.XPATH, "//span[text()='Radio Button']")
    WEB_TABLES_ITEM = (By.XPATH, "//span[text()='Web Tables']")
    BUTTONS_ITEM = (By.XPATH, "//span[text()='Buttons']")
    LINKS_ITEM = (By.XPATH, "//span[text()='Links']")
    BROKEN_LINKS_ITEM = (By.XPATH, "//span[text()='Broken Links - Images']")
    UPLOAD_DOWNLOAD_ITEM = (By.XPATH, "//span[text()='Upload and Download']")
    DYNAMIC_PROPERTIES_ITEM = (By.XPATH, "//span[text()='Dynamic Properties']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self):
        """
        Returns the text of the main header on the page.
        """
        return self.get_element_text(self.HEADER)

    def click_text_box_item(self):
        """
        Clicks on the 'Text Box' item in the left-side menu.
        """
        self.click(self.TEXT_BOX_ITEM)

    def click_check_box_item(self):
        """
        Clicks on the 'Check Box' item in the left-side menu.
        """
        self.click(self.CHECK_BOX_ITEM)

    def click_radio_button_item(self):
        """
        Clicks on the 'Radio Button' item in the left-side menu.
        """
        self.click(self.RADIO_BUTTON_ITEM)

    def click_web_tables_item(self):
        """
        Clicks on the 'Web Tables' item in the left-side menu.
        """
        self.click(self.WEB_TABLES_ITEM)

    def click_buttons_item(self):
        """
        Clicks on the 'Buttons' item in the left-side menu.
        """
        self.click(self.BUTTONS_ITEM)

    def click_links_item(self):
        """
        Clicks on the 'Links' item in the left-side menu.
        """
        self.click(self.LINKS_ITEM)

    def click_broken_links_item(self):
        """
        Clicks on the 'Broken Links - Images' item in the left-side menu.
        """
        self.click(self.BROKEN_LINKS_ITEM)

    def click_upload_download_item(self):
        """
        Clicks on the 'Upload and Download' item in the left-side menu.
        """
        self.click(self.UPLOAD_DOWNLOAD_ITEM)

    def click_dynamic_properties_item(self):
        """
        Clicks on the 'Dynamic Properties' item in the left-side menu.
        """
        self.click(self.DYNAMIC_PROPERTIES_ITEM)
