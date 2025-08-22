from pages.tabs_page import TabsPage


def test_what_tab_content_is_displayed(tabs_page: TabsPage):
    """
    Test Case: Verifies that the 'What' tab content is displayed by default and
    starts with the expected text.
    """
    # Click the 'What' tab to make its content visible
    tabs_page.click_what_tab()
    content_text = tabs_page.get_what_tab_content_text()
    expected_start = "Lorem Ipsum is simply"

    assert content_text.startswith(expected_start), \
        f"The 'What' tab content does not start with the expected text. Found: '{content_text[:20]}...'"


def test_origin_tab_content_is_displayed(tabs_page: TabsPage):
    """
    Test Case: Verifies that clicking the 'Origin' tab displays the correct
    content that starts with the expected text.
    """
    # Click the 'Origin' tab to make its content visible
    tabs_page.click_origin_tab()

    # Get the content of the 'Origin' tab
    content_text = tabs_page.get_origin_tab_content_text()
    expected_start = "Contrary to popular belief"

    assert content_text.startswith(expected_start), \
        f"The 'Origin' tab content does not start with the expected text. Found: '{content_text[:20]}...'"


def test_use_tab_content_is_displayed(tabs_page: TabsPage):
    """
    Test Case: Verifies that clicking the 'Use' tab displays the correct
    content that starts with the expected text.
    """

    # Click the 'Use' tab to make its content visible
    tabs_page.click_use_tab()

    # Get the content of the 'Use' tab
    content_text = tabs_page.get_use_tab_content_text()
    expected_start = "It is a long established fact"

    assert content_text.startswith(expected_start), \
        f"The 'Use' tab content does not start with the expected text. Found: '{content_text[:20]}...'"
