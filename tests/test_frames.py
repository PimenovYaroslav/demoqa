from pages.frames_page import FramesPage


def test_iframes_on_frames_page(frames_page: FramesPage):
    """
    Test suite for handling multiple iframes on the page.
    """
    # Get text from the first frame and verify it
    text_from_frame1 = frames_page.get_text_from_frame(frames_page.FRAME1_ID)
    assert "This is a sample page" in text_from_frame1, \
        f"Expected text 'This is a sample page' not found in Frame 1. Got: {text_from_frame1}"

    # Get text from the second frame and verify it
    text_from_frame2 = frames_page.get_text_from_frame(frames_page.FRAME2_ID)
    assert "This is a sample page" in text_from_frame2, \
        f"Expected text 'This is a sample page' not found in Frame 2. Got: {text_from_frame2}"
