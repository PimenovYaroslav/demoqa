import pytest
from pages.links_page import LinksPage


def test_simple_home_link_opens_new_tab(links_page: LinksPage, driver):
    """
    Tests that the 'Home' link opens a new tab and navigates to the main page.
    """
    initial_window_handle = driver.current_window_handle

    # Click the link using the new POM method
    links_page.click_home_link()

    # Switch to the new tab
    new_window_handle = driver.window_handles[-1]
    driver.switch_to.window(new_window_handle)

    # Verify the URL
    assert driver.current_url == "https://demoqa.com/", "The URL of the new tab is incorrect."

    # Close the new tab and switch back to the original
    driver.close()
    driver.switch_to.window(initial_window_handle)


@pytest.mark.parametrize("link_click_method, expected_message", [
    (lambda page: page.click_created_link(), "Link has responded with staus 201 and status text Created"),
    (lambda page: page.click_no_content_link(), "Link has responded with staus 204 and status text No Content"),
    (lambda page: page.click_moved_link(), "Link has responded with staus 301 and status text Moved Permanently"),
    (lambda page: page.click_bad_request_link(), "Link has responded with staus 400 and status text Bad Request"),
    (lambda page: page.click_unauthorized_link(), "Link has responded with staus 401 and status text Unauthorized"),
    (lambda page: page.click_forbidden_link(), "Link has responded with staus 403 and status text Forbidden"),
    (lambda page: page.click_not_found_link(), "Link has responded with staus 404 and status text Not Found")
])
def test_api_links_display_correct_message(links_page: LinksPage, link_click_method, expected_message):
    """
    Tests that clicking API links displays the correct response message.
    This uses a parameterized test for efficiency and POM methods for reliability.
    """
    link_click_method(links_page)
    assert links_page.get_link_message() == expected_message, \
        f"The message for the clicked link is incorrect"
