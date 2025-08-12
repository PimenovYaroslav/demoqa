from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    Page object model for the DemoQA homepage.
    """
    # Locators
    MAIN_CARDS = (By.XPATH, "//div[@class='card-body']")
    ELEMENTS_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Elements']]")
    FORMS_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Forms']]")
    ALERTS_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Alerts, Frame & Windows']]")
    WIDGETS_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Widgets']]")
    INTERACTIONS_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Interactions']]")
    BOOK_STORE_CARD = (By.XPATH, "//div[@class='card-body' and .//h5[text()='Book Store Application']]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_elements_card(self):
        """
        Finds and clicks the "Elements" card on the homepage.
        """
        self.click(self.ELEMENTS_CARD)

    def click_forms_card(self):
        """
        Finds and clicks the "Forms" card on the homepage.
        """
        self.click(self.FORMS_CARD)

    def click_alerts_card(self):
        """
        Finds and clicks the "Alerts, Frame & Windows" card on the homepage.
        """
        self.click(self.ALERTS_CARD)

    def click_widgets_card(self):
        """
        Finds and clicks the "Widgets" card on the homepage.
        """
        self.click(self.WIDGETS_CARD)

    def click_interactions_card(self):
        """
        Finds and clicks the "Interactions" card on the homepage.
        """
        self.click(self.INTERACTIONS_CARD)

    def click_book_store_card(self):
        """
        Finds and clicks the "Book Store Application" card on the homepage.
        """
        self.click(self.BOOK_STORE_CARD)

    def are_all_main_cards_visible(self) -> bool:
        """
        Checks if all six main cards are visible on the homepage.
        :return: True if all cards are visible, False otherwise.
        """
        card_locators = [
            self.ELEMENTS_CARD,
            self.FORMS_CARD,
            self.ALERTS_CARD,
            self.WIDGETS_CARD,
            self.INTERACTIONS_CARD,
            self.BOOK_STORE_CARD
        ]

        for locator in card_locators:
            if not self.is_element_visible(locator):
                print(f"DEBUG: Card with locator {locator} is not visible.")
                return False
        return True
