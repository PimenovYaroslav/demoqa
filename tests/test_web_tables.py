import pytest
from pages.web_tables_page import WebTablesPage


def test_add_new_record_to_table(web_tables_page: WebTablesPage, web_tables_test_data: dict):
    """
    Tests adding a new record to the table and verifies that it appears correctly.
    This test uses dynamically generated test data from a fixture.
    """
    # 1. Click 'Add' button
    web_tables_page.click_add_button()

    # 2. Fill out and submit the form
    web_tables_page.fill_and_submit_form(**web_tables_test_data)

    # 3. Get the data from the table
    table_data = web_tables_page.get_table_data()

    # 4. Verify that the new record is present in the table
    found = False
    for record in table_data:
        if record['email'] == web_tables_test_data['email']:
            assert record['first_name'] == web_tables_test_data['first_name']
            assert record['last_name'] == web_tables_test_data['last_name']
            assert record['age'] == web_tables_test_data['age']
            assert record['salary'] == web_tables_test_data['salary']
            assert record['department'] == web_tables_test_data['department']
            found = True
            break

    assert found, "The new record was not found in the table."


def test_edit_existing_record(web_tables_page: WebTablesPage):
    """
    Tests editing an existing record and verifies the change.
    We will edit the first user in the table, 'Cierra'.
    """
    initial_name = "Cierra"
    new_name = "Jane"

    # 1. Edit the record
    web_tables_page.edit_record(initial_name, new_name)

    # 2. Get the table data
    table_data = web_tables_page.get_table_data()

    # 3. Verify that the name has been changed
    found = False
    for record in table_data:
        if record['first_name'] == new_name:
            found = True
            break

    assert found, f"The record with the new name '{new_name}' was not found after editing."


def test_delete_record_from_table(web_tables_page: WebTablesPage):
    """
    Tests deleting a record from the table and verifies it's gone.
    We will delete the user 'Cierra' who is in the initial table.
    """
    record_to_delete = "Cierra"

    # 1. Delete the record
    web_tables_page.delete_record(record_to_delete)

    # 2. Get the table data
    table_data = web_tables_page.get_table_data()

    # 3. Verify that the record is no longer in the table
    found = False
    for record in table_data:
        if record['first_name'] == record_to_delete:
            found = True
            break

    assert not found, f"The record '{record_to_delete}' was found after being deleted."
