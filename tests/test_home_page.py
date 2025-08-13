from pages.home_page import HomePage


def test_home_page_title_is_correct(home_page: HomePage):
    """
    Checks that the website title is correct.
    """
    expected_title = "DEMOQA"
    assert home_page.get_page_title() == expected_title, \
        f"Expected title '{expected_title}', but got '{home_page.get_page_title()}'"


def test_main_cards_are_displayed(home_page: HomePage):
    """
    Checks if all six main cards are visible on the homepage.
    """
    assert home_page.are_all_main_cards_visible(), \
        "Not all main cards are visible on the homepage."


def test_card_navigation(home_page: HomePage, driver):
    """
    Checks that clicking on each card navigates to the correct URL.
    """
    # Test Elements card
    home_page.click_elements_card()
    assert driver.current_url.endswith("/elements"), \
        "Did not navigate to the correct URL for the Elements card."
    driver.back()

    # Test Forms card
    home_page.click_forms_card()
    assert driver.current_url.endswith("/forms"), \
        "Did not navigate to the correct URL for the Forms card."
    driver.back()

    # Test Alerts card
    home_page.click_alerts_card()
    assert driver.current_url.endswith("/alertsWindows"), \
        "Did not navigate to the correct URL for the Alerts card."
    driver.back()

    # Test Widgets card
    home_page.click_widgets_card()
    assert driver.current_url.endswith("/widgets"), \
        "Did not navigate to the correct URL for the Widgets card."
    driver.back()

    # Test Interactions card
    home_page.click_interactions_card()
    assert driver.current_url.endswith("/interaction"), \
        "Did not navigate to the correct URL for the Interactions card."
    driver.back()

    # Test Book Store Application card
    home_page.click_book_store_card()
    assert driver.current_url.endswith("/books"), \
        "Did not navigate to the correct URL for the Book Store Application card."
    driver.back()
