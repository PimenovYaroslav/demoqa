
import os
from pages.upload_download_page import UploadDownloadPage
from selenium.common.exceptions import TimeoutException


def test_download_file(upload_download_page: UploadDownloadPage):
    """
    Test for the file download functionality.
    1. Verifies that the file is downloaded to the correct directory.
    2. Deletes the file after the test to avoid conflicts in subsequent runs.
    """
    # Path to the directory where Selenium will download the file (configured in conftest.py)
    download_dir = os.path.join(os.getcwd(), 'downloads')
    expected_file_name = 'sampleFile.jpeg'
    expected_file_path = os.path.join(download_dir, expected_file_name)

    # Remove the file if it already exists to ensure we are testing a new download
    if os.path.exists(expected_file_path):
        os.remove(expected_file_path)

    upload_download_page.click_download_button()

    try:
        # Use the new method from the page object to wait for the file to exist
        upload_download_page.wait_for_downloaded_file(expected_file_path)
    except TimeoutException:
        # If the file is not found, the test will fail with an error
        assert False, "Downloaded file was not found in the downloads directory within the 10-second timeout."

    # Verify that the file exists (this is now guaranteed by the explicit wait)
    assert os.path.exists(expected_file_path), "Downloaded file was not found."

    # Delete the file after the test
    os.remove(expected_file_path)


def test_upload_file(upload_download_page: UploadDownloadPage):
    """
    Test for the file upload functionality.
    1. Creates a temporary file for upload.
    2. Uploads the file and verifies its name on the page.
    3. Deletes the temporary file after the test.
    """
    # Create a temporary file for uploading
    temp_file_name = "test_upload_file.txt"
    temp_file_path = os.path.join(os.getcwd(), temp_file_name)
    with open(temp_file_path, "w") as f:
        f.write("This is a test file for upload.")

    # Upload the file
    upload_download_page.upload_file(temp_file_path)

    # Verify that the file name appears on the page
    uploaded_path_text = upload_download_page.get_uploaded_file_name()
    assert uploaded_path_text.endswith(temp_file_name), \
        f"Expected file name '{temp_file_name}', but got '{uploaded_path_text}'."

    # Delete the temporary file
    os.remove(temp_file_path)
