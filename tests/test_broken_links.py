import pytest
from pages.broken_links_page import BrokenLinksPage


def test_valid_and_broken_links(broken_links_page: BrokenLinksPage):
    """
    Tests that a valid link returns a 200 status code and a broken link returns a 500.
    """
    valid_link_status = broken_links_page.check_link_status_code(broken_links_page.VALID_LINK)
    assert valid_link_status == 200, \
        f"The valid link returned an incorrect status code: {valid_link_status}. Expected 200."

    broken_link_status = broken_links_page.check_link_status_code(broken_links_page.BROKEN_LINK)
    assert broken_link_status == 500, \
        f"The broken link returned an incorrect status code: {broken_link_status}. Expected 500."


def test_valid_and_broken_images(broken_links_page: BrokenLinksPage):
    """
    Tests that a valid image is loaded correctly and a broken image is not.
    """
    is_valid_image_loaded = broken_links_page.is_image_loaded(broken_links_page.VALID_IMAGE)
    assert is_valid_image_loaded, "The valid image failed to load."

    is_broken_image_loaded = broken_links_page.is_image_loaded(broken_links_page.BROKEN_IMAGE)
    assert not is_broken_image_loaded, "The broken image loaded unexpectedly."
