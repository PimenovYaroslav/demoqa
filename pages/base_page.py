from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


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

    def js_click(self, locator: Tuple[str, str]):
        """
        Finds and clicks on an element using JavaScript.
        Use this method as a fallback when ElementClickInterceptedException occurs.
        :param locator: A tuple containing the strategy and the locator value.
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not found within the specified time.")

    def get_element_value(self, locator: tuple[str, str]) -> str:
        """
        Retrieves the 'value' attribute of an element.
        This method is useful for input fields (like <input>) where the text
        is stored in the `value` attribute.
        """
        element = self.find_element(locator)
        return element.get_attribute("value")

    def scroll_to_element(self, locator: Tuple[str, str]):
        """
        Scrolls the element into the viewport using JavaScript.
        :param locator: A tuple containing the strategy and the locator value.
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not found within the specified time.")

    def type_into_element(self, locator: Tuple[str, str], text: str, press_enter: bool = False):
        """
        Types text into an element after ensuring it is visible and enabled.
        Optionally presses Enter after typing.
        :param locator: A tuple containing the strategy and the locator value.
        :param text: The text to be entered.
        :param press_enter: If True, presses Enter after typing.
        """
        self.scroll_to_element(locator)
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            if press_enter:
                element.send_keys(Keys.ENTER)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not visible within the specified time.")

    def send_keys_to_hidden_element(self, locator: Tuple[str, str], file_path: str):
        """
        Sends the file path to a hidden input element. This method is ideal
        for file uploads, as `<input type='file'>` elements are often
        hidden on the page.
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.send_keys(file_path)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not found within the specified time.")

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


    def wait_for_visibility_of_element(self, locator: tuple[str, str], timeout: int = None):
        """
        Explicitly waits for an element to become visible on the page.
        This is useful for elements that appear dynamically.
        :param locator: A tuple (By.ID, "id_name").
        :param timeout: Optional timeout in seconds for this specific wait.
                        If not provided, uses the default timeout.
        """
        wait_for_this = WebDriverWait(self.driver, timeout) if timeout else self.wait
        wait_for_this.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        """
        Waits for an element to become invisible and returns True if successful.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            print(f"[Timeout] Element {locator} is still visible after {timeout} seconds")
            return False

    def get_element_text(self, locator: Tuple[str, str]) -> str:
        """
        Finds an element and returns its text.
        :param locator: A tuple containing the strategy and the locator value.
        :return: The text of the element.
        """
        return self.find_element(locator).text

    def select_from_dropdown(self, locator: Tuple[str, str], value: str, by_type: str = "text"):
        """
        Selects an option from a <select> dropdown element.

        Args:
            locator: A tuple containing (By.strategy, "locator_value") for the dropdown element.
            value: The value to select.
            by_type: The selection method ("text", "value", or "index"). Defaults to "text".

        Raises:
            ValueError: If the provided by_type is not supported.
        """
        dropdown_element = self.find_element(locator)
        select = Select(dropdown_element)

        if by_type == "text":
            select.select_by_visible_text(value)
        elif by_type == "value":
            select.select_by_value(value)
        elif by_type == "index":
            select.select_by_index(int(value))
        else:
            raise ValueError(f"Invalid selection type: '{by_type}'. Supported values are 'text', 'value', 'index'.")

    def get_current_window_handle(self):
        """
        Returns the handle of the current browser window.
        """
        return self.driver.current_window_handle

    def get_all_window_handles(self):
        """
        Returns a list of all available window handles.
        """
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """
        Switches the WebDriver's focus to a specified window.

        Args:
            window_handle: The handle of the window to switch to.
        """
        self.driver.switch_to.window(window_handle)

    def close_current_window(self):
        """
        Closes the current browser window or tab.
        """
        self.driver.close()

    def get_current_url(self):
        """
        Returns the URL of the current page.
        """
        return self.driver.current_url

    def accept_alert(self):
        """Accepts (clicks OK on) a standard alert."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Dismisses (clicks Cancel on) a confirm or standard alert."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def send_keys_to_alert(self, keys: str):
        """Sends keys to a prompt alert and accepts it."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(keys)
        alert.accept()
