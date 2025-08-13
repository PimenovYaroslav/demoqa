from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, List


class BasePage:
    """
    This class is the parent for all pages.
    It contains all the common methods and functionalities for all pages.
    """

    def __init__(self, driver):
        """
        Initializes the BasePage object.
        :param driver: The WebDriver instance.
        """
        self.driver = driver
        # Use explicit waits for better control over element loading
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url: str):
        """
        Navigates the browser to the specified URL.
        :param url: The URL to open.
        """
        self.driver.get(url)

    def get_page_title(self):
        """Returns the title of the current page."""
        return self.driver.title

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Finds and returns a visible element using an explicit wait.
        :param locator: A tuple containing the strategy and the locator value (e.g., (By.ID, "some_id")).
        :return: The WebElement object if found and visible.
        :raises TimeoutException: If the element is not found within the specified time.
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found or is not visible.")

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Finds and returns a list of visible elements using an explicit wait.
        :param locator: A tuple containing the strategy and the locator value.
        :return: A list of WebElement objects if found and visible.
        :raises TimeoutException: If no elements are found within the specified time.
        """
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Elements with locator {locator} not found or are not visible.")

    def click(self, locator: Tuple[str, str]):
        """
        Finds and clicks on an element only after it becomes clickable and scrolled into view.
        :param locator: A tuple containing the strategy and the locator value.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not clickable within the specified time.")

    def type_into_element(self, locator: Tuple[str, str], text: str):
        """
           Finds an element, scrolls it into view, and sends text to it.
           :param locator: A tuple containing the strategy and the locator value.
           :param text: The text to send to the element.
           """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """
        Checks if an element is visible on the page.
        Does not raise an exception if the element is not found.
        :param locator: A tuple containing the strategy and the locator value.
        :return: True if the element is visible, False otherwise.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator: Tuple[str, str]) -> str:
        """
        Finds an element and returns its text.
        :param locator: A tuple containing the strategy and the locator value.
        :return: The text of the element.
        """
        return self.find_element(locator).text
