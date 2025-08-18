import random

from pages.auto_complete_page import AutoCompletePage

# Pre-defined list of valid colors for testing
VALID_COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Indigo", "Magenta"]


def test_enter_single_value(auto_complete_page: AutoCompletePage):
    """
    Test case to verify that a single value can be successfully entered and selected
    in the single-color auto-complete field by typing the first two letters.
    """
    random_color = random.choice(VALID_COLORS)
    # Use the first two letters of the random color
    partial_string = random_color[:2]
    auto_complete_page.enter_single_value(partial_string)

    # Assert that the randomly chosen full color is selected.
    assert auto_complete_page.is_single_value_selected(random_color), \
        f"Expected '{random_color}' to be selected after entering '{partial_string}', but it was not visible."


def test_enter_multiple_values(auto_complete_page: AutoCompletePage):
    """
    Test case to verify that multiple random values can be entered and selected
    in the multicolor auto-complete field by typing the first two letters of each.
    """
    # Choose two distinct random colors for this test
    colors_to_select = random.sample(VALID_COLORS, 2)
    color1, color2 = colors_to_select[0], colors_to_select[1]

    # Enter the first two letters of the first color
    partial_string1 = color1[:2]
    auto_complete_page.enter_multi_value(partial_string1)

    # Enter the first two letters of the second color
    partial_string2 = color2[:2]
    auto_complete_page.enter_multi_value(partial_string2)

    selected = auto_complete_page.get_selected_multi_values()

    # Assert that both randomly chosen full colors are present in the list of selected values.
    assert color1 in selected and color2 in selected, \
        f"Expected '{color1}' and '{color2}' to be selected, but found: {selected}"


def test_remove_multi_value(auto_complete_page: AutoCompletePage):
    """
    Test case to verify that the remove button correctly deletes the last
    selected value in the multicolor auto-complete field, using random colors.
    """
    # Choose two distinct random colors for the test
    colors_to_use = random.sample(VALID_COLORS, 2)
    color_to_keep = colors_to_use[0]
    color_to_remove = colors_to_use[1]

    auto_complete_page.enter_multi_value(color_to_keep)
    auto_complete_page.enter_multi_value(color_to_remove)
    auto_complete_page.remove_last_multi_value()
    selected = auto_complete_page.get_selected_multi_values()

    # Assert that the second color (the one to be removed) is no longer present,
    # and the first color is still there.
    assert color_to_remove not in selected and color_to_keep in selected, \
        f"Expected '{color_to_remove}' to be removed, but it is still in the list, " \
        f"and/or '{color_to_keep}' is missing. List: {selected}"


def test_suggestions_appear(auto_complete_page: AutoCompletePage):
    """
    Test case to verify that suggestions appear in the dropdown
    when a partial value (two letters) is entered into the single-color field, using a random color.
    """
    # Choose a random color and get its first two letters
    random_color = random.choice(VALID_COLORS)
    # Ensure the color has at least two letters to avoid an IndexError
    partial_string = random_color[:2] if len(random_color) >= 2 else random_color[0]

    auto_complete_page.enter_single_value(partial_string, press_enter=False)
    suggestions = auto_complete_page.get_suggestions()

    # Assert that the full randomly chosen color is a suggestion.
    assert any(random_color in s for s in suggestions), \
        f"Expected '{random_color}' to be a suggestion after typing '{partial_string}', but found: {suggestions}"
