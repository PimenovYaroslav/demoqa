
from pages.buttons_page import ButtonsPage


def test_double_click_button(buttons_page: ButtonsPage):
    """
    Tests that double-clicking the 'Double Click Me' button displays the correct message.
    """
    buttons_page.double_click_on_button()
    assert buttons_page.get_double_click_message() == "You have done a double click", \
        "The message for double-clicking is incorrect."


def test_right_click_button(buttons_page: ButtonsPage):
    """
    Tests that right-clicking the 'Right Click Me' button displays the correct message.
    """
    buttons_page.right_click_on_button()
    assert buttons_page.get_right_click_message() == "You have done a right click", \
        "The message for right-clicking is incorrect."


def test_dynamic_click_button(buttons_page: ButtonsPage):
    """
    Tests that a regular click on the 'Click Me' button displays the correct message.
    """
    buttons_page.click_on_button()
    assert buttons_page.get_dynamic_click_message() == "You have done a dynamic click", \
        "The message for a regular click is incorrect."

