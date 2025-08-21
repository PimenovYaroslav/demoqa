import random
from pages.slider_page import SliderPage


def test_slider_moves_to_random_value(slider_page: SliderPage):
    """
    Test Case: Verifies that the slider can be moved to a random position
    and the value is displayed correctly.
    """
    # Generate a random target value for the slider
    target_value = random.randint(0, 100)

    # Move the slider using the method from the Page Object
    slider_page.move_slider_with_keys(target_value)

    # Get the final value from the page using a Page Object method
    final_value = slider_page.get_slider_value()

    assert final_value == target_value, \
        f"Error! Expected value {target_value}, but got {final_value}"

