import os


def test_fill_and_submit_practice_form(practice_form_page, generated_form_data):
    """
    Fills out the practice form using dynamically generated data, submits it,
    and then verifies the submitted data in the confirmation modal.
    """
    # 1. Fill the form with data from the fixture
    practice_form_page.set_first_name(generated_form_data["first_name"])
    practice_form_page.set_last_name(generated_form_data["last_name"])
    practice_form_page.set_email(generated_form_data["email"])
    practice_form_page.set_gender(generated_form_data["gender"])
    practice_form_page.set_mobile_number(generated_form_data["mobile_number"])
    practice_form_page.set_date_of_birth(
        generated_form_data["day_of_birth"],
        generated_form_data["month_of_birth"],
        generated_form_data["year_of_birth"]
    )
    practice_form_page.add_subjects(generated_form_data["subjects"])
    practice_form_page.set_hobbies(generated_form_data["hobbies"])
    practice_form_page.set_current_address(generated_form_data["address"])

    # Create the full path to the picture file for upload
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    picture_full_path = os.path.join(project_root, generated_form_data["file_to_upload"])

    # Check if the file exists before attempting to upload it
    if os.path.exists(picture_full_path):
        practice_form_page.upload_picture(picture_full_path)
    else:
        # A warning is printed but the test continues as upload is not critical
        print(f"Warning: The file '{picture_full_path}' does not exist. Skipping picture upload.")

    # Select the state and city using the dynamically generated data
    practice_form_page.set_state_and_city(generated_form_data["state"], generated_form_data["city"])

    # 2. Submit the form
    practice_form_page.submit_form()

    # 3. Verify the data in the submission modal
    submission_data = practice_form_page.verify_submission_data()

    # Define expected values based on the generated data
    expected_full_name = f"{generated_form_data['first_name']} {generated_form_data['last_name']}"
    expected_birth_date = (
        f"{generated_form_data['day_of_birth']} "
        f"{generated_form_data['month_of_birth']},"
        f"{generated_form_data['year_of_birth']}"
    )
    expected_subjects = ", ".join(generated_form_data["subjects"])
    expected_hobbies = ", ".join(generated_form_data["hobbies"])
    expected_state_city = f"{generated_form_data['state']} {generated_form_data['city']}"

    # Assertions to validate the submitted data
    assert submission_data["Student Name"] == expected_full_name, "Student name does not match."
    assert submission_data["Student Email"] == generated_form_data["email"], "Student email does not match."
    assert submission_data["Gender"] == generated_form_data["gender"], "Gender does not match."
    assert submission_data["Mobile"] == generated_form_data["mobile_number"], "Mobile number does not match."
    assert submission_data["Date of Birth"] == expected_birth_date, "Date of Birth does not match."
    assert submission_data["Subjects"] == expected_subjects, "Subjects do not match."
    assert set(submission_data["Hobbies"]) == set(expected_hobbies), "Hobbies do not match."

    # Only assert picture upload if the file existed
    if os.path.exists(picture_full_path):
        assert submission_data["Picture"] == os.path.basename(picture_full_path), "Picture file name does not match."

    assert submission_data["Address"] == generated_form_data["address"], "Address does not match."
    assert submission_data["State and City"] == expected_state_city, "State and City do not match."
