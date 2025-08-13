import pytest
from pages.check_box_page import CheckBoxPage


def test_select_all_checkboxes_and_verify(check_box_page: CheckBoxPage):
    """
    Checks that all checkboxes are selected when the 'Home' checkbox is clicked
    and verifies the result message.
    """
    check_box_page.expand_all_folders()
    check_box_page.click_home_checkbox()

    expected_names = check_box_page.get_all_checkboxes_names()
    actual_selected_names = check_box_page.get_selected_names_from_result()

    assert sorted(actual_selected_names) == sorted(expected_names), \
        "The selected checkboxes do not match the expected list."


def test_select_random_checkboxes_and_verify(check_box_page: CheckBoxPage):
    """
    Checks that a randomly selected checkbox and its children are correctly reflected
    in the result message.
    """
    selected_names = check_box_page.select_random_checkboxes_and_get_result()
    result_names = check_box_page.get_selected_names_from_result()

    assert sorted(selected_names) == sorted(result_names), \
        "The selected random checkboxes do not match the expected result."


