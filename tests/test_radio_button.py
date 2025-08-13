import pytest
from pages.radio_button_page import RadioButtonPage
from selenium.common.exceptions import TimeoutException


def test_select_yes_radio_button(radio_button_page: RadioButtonPage):
    """
    Tests that selecting the 'Yes' radio button displays the correct success message.
    """
    radio_button_page.click_radio_button('Yes')
    assert radio_button_page.get_result_message() == "You have selected Yes", \
        "The result message for 'Yes' radio button is incorrect."


def test_select_impressive_radio_button(radio_button_page: RadioButtonPage):
    """
    Tests that selecting the 'Impressive' radio button displays the correct success message.
    """
    radio_button_page.click_radio_button('Impressive')
    assert radio_button_page.get_result_message() == "You have selected Impressive", \
        "The result message for 'Impressive' radio button is incorrect."


def test_no_radio_button_is_unclickable(radio_button_page: RadioButtonPage):
    """
    Tests that the 'No' radio button is disabled and does not produce a result message.
    The test will pass if a TimeoutException is raised, as the result message will not appear.
    """
    radio_button_page.click_radio_button('No')

    # Assert that the result message does not appear.
    try:
        radio_button_page.get_result_message()
        # This line should not be reached if the test is successful
        pytest.fail("The 'No' radio button was clicked and a message appeared, but it should be unclickable.")
    except TimeoutException:
        # This is the expected behavior, so the test passes
        pass
