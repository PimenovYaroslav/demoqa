import requests
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from typing import Tuple


class BrokenLinksPage(BasePage):
    """
    Page object model for the DemoQA Broken Links - Images page.
    """
    # Locators for images
    VALID_IMAGE = (By.XPATH, "//img[contains(@src, 'Toolsqa.jpg')]")
    BROKEN_IMAGE = (By.XPATH, "//img[contains(@src, 'no-image-available.jpg')]")

    # Locators for links
    VALID_LINK = (By.XPATH, "//a[text()='Click Here for Valid Link']")
    BROKEN_LINK = (By.XPATH, "//a[text()='Click Here for Broken Link']")

    def __init__(self, driver):
        super().__init__(driver)

    def check_link_status_code(self, locator: Tuple[str, str]) -> int:
        """
        Retrieves the href attribute of a link and checks its HTTP status code.
        :param locator: The locator of the link element.
        :return: The HTTP status code as an integer.
        """
        link_element = self.find_element(locator)
        link_url = link_element.get_attribute("href")
        try:
            response = requests.head(link_url, allow_redirects=True, timeout=5)
            return response.status_code
        except requests.exceptions.RequestException:
            return 0  # Return 0 for connection errors

    def is_image_loaded(self, locator: Tuple[str, str]) -> bool:
        """
        Checks if an image is successfully loaded by evaluating its naturalWidth.
        A loaded image will have a naturalWidth greater than 0.
        :param locator: The locator of the image element.
        :return: True if the image is loaded, False otherwise.
        """
        try:
            image_element = self.find_element(locator)
            # Use JavaScript to check the image's naturalWidth
            return self.driver.execute_script("return arguments[0].naturalWidth > 0", image_element)
        except TimeoutException:
            # If the element is not found, the image is considered not loaded.
            return False
