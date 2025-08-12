from pages.elements_page import ElementsPage


def test_elements_page_header_is_correct(elements_page: ElementsPage):
    """
    Checks that the header on the Elements page is correct.
    """
    assert elements_page.get_header_text() == "Elements"


def test_navigate_to_text_box(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Text Box' item navigates to the correct URL.
    """
    elements_page.click_text_box_item()
    assert driver.current_url.endswith("/text-box")


def test_navigate_to_check_box(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Check Box' item navigates to the correct URL.
    """
    elements_page.click_check_box_item()
    assert driver.current_url.endswith("/checkbox")


def test_navigate_to_radio_button(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Radio Button' item navigates to the correct URL.
    """
    elements_page.click_radio_button_item()
    assert driver.current_url.endswith("/radio-button")


def test_navigate_to_web_tables(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Web Tables' item navigates to the correct URL.
    """
    elements_page.click_web_tables_item()
    assert driver.current_url.endswith("/webtables")


def test_navigate_to_buttons(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Buttons' item navigates to the correct URL.
    """
    elements_page.click_buttons_item()
    assert driver.current_url.endswith("/buttons")


def test_navigate_to_links(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Links' item navigates to the correct URL.
    """
    elements_page.click_links_item()
    assert driver.current_url.endswith("/links")


def test_navigate_to_broken_links(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Broken Links - Images' item navigates to the correct URL.
    """
    elements_page.click_broken_links_item()
    assert driver.current_url.endswith("/broken")


def test_navigate_to_upload_download(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Upload and Download' item navigates to the correct URL.
    """
    elements_page.click_upload_download_item()
    assert driver.current_url.endswith("/upload-download")


def test_navigate_to_dynamic_properties(elements_page: ElementsPage, driver):
    """
    Checks that clicking the 'Dynamic Properties' item navigates to the correct URL.
    """
    elements_page.click_dynamic_properties_item()
    assert driver.current_url.endswith("/dynamic-properties")