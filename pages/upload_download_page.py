import os
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class UploadDownloadPage(BasePage):
    """
    Page object model for the Upload and Download page.
    """
    # Locators for the elements on the page
    DOWNLOAD_BUTTON = (By.ID, "downloadButton")
    UPLOAD_INPUT = (By.ID, "uploadFile")
    UPLOADED_FILE_PATH_TEXT = (By.ID, "uploadedFilePath")

    def __init__(self, driver):
        super().__init__(driver)

    def click_download_button(self):
        """
        Clicks the 'Download' button.
        """
        self.click(self.DOWNLOAD_BUTTON)

    def upload_file(self, file_path: str):
        """
        Uploads a file by sending the file path to the upload input element.
        :param file_path: The full path to the file to be uploaded.
        """
        # The input element is of type 'file', so we can send the path directly
        self.find_element(self.UPLOAD_INPUT).send_keys(file_path)

    def get_uploaded_file_name(self) -> str:
        """
        Returns the text of the element that displays the uploaded file path.
        :return: The name of the uploaded file as a string.
        """
        return self.get_element_text(self.UPLOADED_FILE_PATH_TEXT)

    def wait_for_downloaded_file(self, file_path: str, timeout: int = 10):
        """
        Waits for a file to appear at the specified path.
        :param file_path: The full path to the file to wait for.
        :param timeout: The maximum time to wait in seconds.
        :raises TimeoutException: If the file is not found within the timeout.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda d: os.path.exists(file_path))
        except TimeoutException:
            raise TimeoutException(
                f"Downloaded file was not found at '{file_path}' within the {timeout}-second timeout.")
