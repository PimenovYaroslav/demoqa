from pages.nested_frames_page import NestedFramesPage


def test_nested_frames_text(nested_frames_page: NestedFramesPage):
    """
    Test to verify the text in the parent and child iframes.
    """
    # Verification of the text in the parent frame
    parent_text = nested_frames_page.get_text_from_parent_frame()
    expected_parent_text = "Parent frame"
    assert expected_parent_text in parent_text, f"Error! Expected text '{expected_parent_text}' not found."

    # Verification of the text in the child frame
    child_text = nested_frames_page.get_text_from_child_frame()
    expected_child_text = "Child Iframe"
    assert expected_child_text in child_text, f"Error! Expected text '{expected_child_text}' not found."
