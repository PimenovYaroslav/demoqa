import pytest
from pages.dynamic_properties_page import DynamicPropertiesPage


def test_enable_button(dynamic_properties_page: DynamicPropertiesPage):
    """
    Test verifies that the button becomes enabled after 5 seconds.
    """
    assert dynamic_properties_page.check_enable_button(), "Button did not become enabled after 5 seconds."


def test_color_change(dynamic_properties_page: DynamicPropertiesPage):
    """
    Test verifies that the button's text color changes to red after 5 seconds.

    The logic of the test is as follows:
    1. Get the initial color of the button before any changes.
    2. Wait for the color change to occur and assert that the button becomes red.
    3. Get the new color of the button after the change.
    4. Assert that the initial and new colors are different, confirming a change has occurred.
    """
    # Step 1: Get the initial color of the button
    initial_color = dynamic_properties_page.get_button_color()

    # Step 2: Wait for the button to change color to red and assert the change
    assert dynamic_properties_page.check_color_change(), "The button's color did not change to red."

    # Step 3: Get the new color of the button
    new_color = dynamic_properties_page.get_button_color()

    # Step 4: Assert that the initial color is not the same as the new color
    assert initial_color != new_color, "The button's color did not change from its initial state."


def test_button_becomes_visible(dynamic_properties_page: DynamicPropertiesPage):
    """
    Test verifies that the button becomes visible after 5 seconds.
    """
    assert dynamic_properties_page.check_visible_after_button(), "Button did not become visible after 5 seconds."


def test_static_text_is_displayed(dynamic_properties_page: DynamicPropertiesPage):
    """
    Test verifies that the static text element is displayed immediately on page load.
    """
    assert dynamic_properties_page.is_text_with_random_id_displayed(), "The static text is not displayed."
