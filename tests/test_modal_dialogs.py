from pages.modal_dialogs_page import ModalDialogsPage


def test_small_modal(modal_dialogs_page: ModalDialogsPage):
    """
    Test case to verify the functionality of the small modal dialog.

    Steps:
    1. Open the small modal.
    2. Verify that the modal is visible.
    3. Get the modal's content (title and body).
    4. Verify that the title is correct.
    5. Verify that the body text is not empty.
    6. Close the modal.
    7. Verify that the modal is no longer visible.
    """
    modal_dialogs_page.open_small_modal()
    assert modal_dialogs_page.is_small_modal_visible(), "Small modal is not visible"

    content = modal_dialogs_page.get_small_modal_content()
    assert content["title"] == "Small Modal", "Small modal title incorrect"
    assert len(content["body"]) > 0, "Small modal body is empty"

    modal_dialogs_page.close_small_modal()
    assert not modal_dialogs_page.is_small_modal_visible(), "Small modal did not close"


def test_large_modal(modal_dialogs_page: ModalDialogsPage):
    """
    Test case to verify the functionality of the large modal dialog.

    Steps:
    1. Open the large modal.
    2. Verify that the modal is visible.
    3. Get the modal's content (title and body).
    4. Verify that the title is correct.
    5. Verify that the body text is not empty.
    6. Close the modal.
    7. Verify that the modal is no longer visible.
    """
    modal_dialogs_page.open_large_modal()
    assert modal_dialogs_page.is_large_modal_visible(), "Large modal is not visible"

    content = modal_dialogs_page.get_large_modal_content()
    assert content["title"] == "Large Modal", "Large modal title incorrect"
    assert len(content["body"]) > 0, "Large modal body is empty"

    modal_dialogs_page.close_large_modal()
    assert not modal_dialogs_page.is_large_modal_visible(), "Large modal did not close"
