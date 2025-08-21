import random
from pages.progress_bar_page import ProgressBarPage


def test_progress_bar_completes_and_resets(progress_bar_page: ProgressBarPage):
    """
    Test Case: Verifies that the progress bar successfully completes its
    progression to 100% and the "Reset" button appears.
    """
    # Start the progress bar
    progress_bar_page.start_progress()

    # Wait for the progress to reach 100%
    progress_bar_page.wait_for_completion()

    # 1. Verify that the progress bar value is exactly 100
    final_value = progress_bar_page.get_progress_value()
    assert final_value == 100, \
        f"Error! Expected final value to be 100, but got {final_value}"

    # 2. Verify that the "Reset" button is now visible
    assert progress_bar_page.is_reset_button_visible(), "Error! The 'Reset' button is not visible after completion."


def test_progress_bar_can_be_stopped_and_restarted(progress_bar_page: ProgressBarPage):
    """
    Test Case: Verifies that the progress bar can be stopped,
    restarted, and then successfully reaches 100% without using fixed waits.
    """
    random_stop = random.randint(10, 80)
    # Start the progress bar
    progress_bar_page.start_progress()

    # Wait until the progress bar reaches a value greater than 25%
    progress_bar_page.wait_for_value_to_exceed(random_stop)

    # Stop the progress at an intermediate value
    progress_bar_page.stop_progress()
    stopped_value = progress_bar_page.get_progress_value()

    # 1. Verify that the progress bar was stopped at an intermediate value
    assert random_stop < stopped_value < 100, \
        f"Error! Expected the progress bar to stop between 25 and 100, but got {stopped_value}"

    # Restart the progress bar to completion
    progress_bar_page.start_progress()

    # Wait for the progress to reach 100%
    progress_bar_page.wait_for_completion()

    # 2. Verify that the progress bar value is exactly 100
    final_value = progress_bar_page.get_progress_value()
    assert final_value == 100, f"Error! Expected final value to be 100, but got {final_value}"


