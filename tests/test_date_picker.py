from pages.date_picker_page import DatePickerPage
from datetime import datetime


def test_select_date(date_picker_page: DatePickerPage, random_date_time_data: dict):
    """
    Test case to select a random date in the basic date picker using a fixture.
    """
    # Unpack the random data from the fixture
    random_year = random_date_time_data["year"]
    random_month = random_date_time_data["month"]
    random_day = random_date_time_data["day"]
    # Use the page object method to select the random date
    date_picker_page.select_date(day=str(int(random_day)), month=random_month, year=random_year)
    # Get the value from the input field
    value = date_picker_page.get_selected_date_value()

    # Define the expected month format (e.g., '08' for August)
    expected_month_number = datetime.strptime(random_month, "%B").strftime("%m")

    # Assert that the expected date is in the input field's value
    expected_date_part = f"{expected_month_number}/{random_day}/{random_year}"

    assert expected_date_part in value, \
        f"Expected '{expected_date_part}' in '{value}' but it was not found."


def test_select_date_time(date_picker_page: DatePickerPage, random_date_time_data: dict):
    """
    Test case to select a random date and time in the datetime picker using a fixture.
    """
    # Unpack the random data from the fixture
    random_year = random_date_time_data["year"]
    random_month = random_date_time_data["month"]
    random_day = random_date_time_data["day"]
    random_time_24h = random_date_time_data["time_24h"]
    expected_time_12h = random_date_time_data["expected_time_12h"]

    # Use the page object method to select the random date and time
    date_picker_page.select_date_time(
        day=str(int(random_day)),
        month=random_month,
        year=random_year,
        time=random_time_24h
    )

    # Get the value from the input field
    value = date_picker_page.get_selected_date_time_value()

    # Assert that the expected date and time values are present in the string
    expected_date_part = f"{random_month} {str(int(random_day))}, {random_year}"

    assert expected_date_part in value, \
        f"Expected '{expected_date_part}' in '{value}' but it was not found."
    assert expected_time_12h in value, \
        f"Expected '{expected_time_12h}' in '{value}' but it was not found."
