from pages.browser_windows_page import BrowserWindowsPage


def test_new_tab_sequence(browser_windows_page: BrowserWindowsPage):
    """
    Executes a full test sequence for the 'New Tab' button:
    1. Clicks the button and verifies a new tab opens.
    2. Switches to the new tab and checks its content.
    3. Closes the new tab and returns to the original.
    4. Verifies the browser has returned to the original URL.
    Args: browser_windows_page (BrowserWindowsPage): The Page Object instance provided by the fixture.
    """
    # 1. Store the original window handle and click the button
    original_window = browser_windows_page.get_current_window_handle()
    browser_windows_page.click_new_tab_button()

    # 2. Get all window handles and verify that a new tab has opened
    all_windows = browser_windows_page.get_all_window_handles()
    assert len(all_windows) == 2, "Expected a new tab to open."

    # 3. Find the new tab handle and switch to it
    new_tab_handle = [handle for handle in all_windows if handle != original_window][0]
    browser_windows_page.switch_to_window(new_tab_handle)

    # 4. Check the content of the new tab using the updated method
    new_tab_text = browser_windows_page.get_new_window_text()
    assert "This is a sample page" in new_tab_text, "The new tab does not contain the expected text."

    # 5. Get and verify the new tab's URL
    new_tab_url = browser_windows_page.get_current_url()
    assert "sample" in new_tab_url, "The new tab's URL is incorrect."

    # 6. Close the new tab and switch back to the original
    browser_windows_page.close_current_window()
    browser_windows_page.switch_to_window(original_window)

    # 7. Verify the driver has returned to the initial page
    original_url = browser_windows_page.get_current_url()
    assert "browser-windows" in original_url, "The driver failed to return to the original page."


def test_new_window_sequence(browser_windows_page: BrowserWindowsPage):
    """
    Performs a full test sequence for the 'New Window' button.
    1. Clicks the button and verifies a new window opens.
    2. Switches to the new window and checks its content.
    3. Closes the new window and returns to the original.
    4. Verifies the browser has returned to the original URL.

    Args:
        browser_windows_page (BrowserWindowsPage): The Page Object instance provided by the fixture.
    """
    # 1. Store the original window handle and click the button
    original_window = browser_windows_page.get_current_window_handle()
    browser_windows_page.click_new_window_button()

    # 2. Get all window handles and verify that a new window has opened
    all_windows = browser_windows_page.get_all_window_handles()
    assert len(all_windows) == 2, "Expected a new window to open."

    # 3. Find the new window handle and switch to it
    new_window_handle = [handle for handle in all_windows if handle != original_window][0]
    browser_windows_page.switch_to_window(new_window_handle)

    # 4. Check the content of the new window
    new_window_text = browser_windows_page.get_new_window_text()
    assert "This is a sample page" in new_window_text, "The new window does not contain the expected text."

    # 5. Get and verify the new window's URL
    new_window_url = browser_windows_page.get_current_url()
    assert "sample" in new_window_url, "The new window's URL is incorrect."

    # 6. Close the new window and switch back to the original
    browser_windows_page.close_current_window()
    browser_windows_page.switch_to_window(original_window)

    # 7. Verify the driver has returned to the initial page
    original_url = browser_windows_page.get_current_url()
    assert "browser-windows" in original_url, "The driver failed to return to the original page."


def test_new_window_message_sequence(browser_windows_page: BrowserWindowsPage):
    """
    Tests the full lifecycle of opening, switching to, and closing a new browser window.

    This test validates the core functionality of managing multiple browser windows, ensuring that:
    1. A new window is successfully opened after a button click.
    2. The WebDriver can switch its context to the new window.
    3. The new window can be closed.
    4. The WebDriver can successfully switch back to the original window.

    This approach verifies the robust behavior of the browser and is independent of any content within the new window.
    """
    # Store the handle of the original window.
    original_window = browser_windows_page.get_current_window_handle()

    # Click the button to open the new message window.
    browser_windows_page.click_new_window_message_button()

    # Find the handle of the new window.
    all_windows = browser_windows_page.get_all_window_handles()
    new_window_handle = [h for h in all_windows if h != original_window][0]

    # Assert that the new window handle exists.
    assert new_window_handle is not None, "New message window did not open."

    # Switch to the new window.
    browser_windows_page.switch_to_window(new_window_handle)

    # Close the new window.
    browser_windows_page.close_current_window()

    # Switch back to the original window.
    browser_windows_page.switch_to_window(original_window)

    # Verify that the browser is back on the original page.
    assert "browser-windows" in browser_windows_page.get_current_url(), "Did not return to the original window."
