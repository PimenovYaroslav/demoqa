import pytest
from pages.accordion_page import AccordionPage


def test_all_accordion_sections_can_be_opened(accordion_page: AccordionPage):
    """
    Test to check that each accordion section can be opened and its content is displayed.
    Also verifies that previous sections collapse when a new one is opened.
    """
    # --- Test Section 1 ---
    accordion_page.open_section_1()
    assert accordion_page.is_section_1_expanded(), "Error! Section 1 did not expand."
    assert len(accordion_page.get_section_1_content()) > 0, "Error! Section 1 content is empty."

    # --- Test Section 2 ---
    accordion_page.open_section_2()
    assert accordion_page.is_section_2_expanded(), "Error! Section 2 did not expand."
    assert accordion_page.is_section_1_collapsed(), "Error! Previous section 1 did not collapse."
    assert len(accordion_page.get_section_2_content()) > 0, "Error! Section 2 content is empty."

    # --- Test Section 3 ---
    accordion_page.open_section_3()
    assert accordion_page.is_section_3_expanded(), "Error! Section 3 did not expand."
    assert accordion_page.is_section_1_collapsed(), "Error! Previous section 1 did not collapse."
    assert accordion_page.is_section_2_collapsed(), "Error! Previous section 2 did not collapse."
    assert len(accordion_page.get_section_3_content()) > 0, "Error! Section 3 content is empty."

