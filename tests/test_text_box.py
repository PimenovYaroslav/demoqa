import pytest
from pages.text_box_page import TextBoxPage


def test_fill_form_and_check_output(text_box_page: TextBoxPage, test_data):
    """
    Tests filling out the form with generated fake data,
    submitting it, and verifying that the output data matches the input.
    """
    # Normalize the fake address data by removing newlines for a correct comparison
    normalized_current_address = test_data["current_address"].replace('\n', ' ')
    normalized_permanent_address = test_data["permanent_address"].replace('\n', ' ')

    # Fill the form with the provided data
    text_box_page.fill_form(
        test_data["full_name"],
        test_data["email"],
        normalized_current_address,
        normalized_permanent_address
    )

    # Submit the form
    text_box_page.submit_form()

    # Retrieve the output data after submission
    output_data = text_box_page.get_output_text()

    # Assert that the input and output data match
    assert "Name:" in output_data["name"], \
        "Output name is missing 'Name:' prefix."
    assert test_data["full_name"] in output_data["name"], \
        "Full name in output does not match input."

    assert "Email:" in output_data["email"], \
        "Output email is missing 'Email:' prefix."
    assert test_data["email"] in output_data["email"], \
        "Email in output does not match input."

    assert "Current Address :" in output_data["current_address"], \
        "Output current address is missing 'Current Address :' prefix."
    assert normalized_current_address in output_data["current_address"], \
        "Current address in output does not match input."

    assert "Permananet Address :" in output_data["permanent_address"], \
        "Output permanent address is missing 'Permananet Address :' prefix."
    assert normalized_permanent_address in output_data["permanent_address"], \
        "Permanent address in output does not match input."
