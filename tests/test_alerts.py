from pages.alerts_page import AlertsPage


def test_alerts_on_alerts_page(alerts_page: AlertsPage):
    """
    Test suite for handling various types of JavaScript alerts.
    """
    # Test a standard alert
    alerts_page.click_alert_button()
    alerts_page.accept_alert()

    # Test an alert with a timer
    alerts_page.click_timer_alert_button()
    alerts_page.accept_alert()

    # Test a confirm alert (accept)
    alerts_page.click_confirm_button()
    alerts_page.accept_alert()
    assert "You selected Ok" in alerts_page.get_confirm_result()

    # Test a confirm alert (dismiss)
    alerts_page.click_confirm_button()
    alerts_page.dismiss_alert()
    assert "You selected Cancel" in alerts_page.get_confirm_result()

    # Test a prompt alert (send keys and accept)
    test_name = "Slava"
    alerts_page.click_prompt_button()
    alerts_page.send_keys_to_alert(test_name)
    assert f"You entered {test_name}" in alerts_page.get_prompt_result()
