from playwright.sync_api import expect
from playwright._impl._page import Page

from speak_ukrainian.src.web.pages.home_page import HomePage


# TUA-314
def test_placeholder_disappear_while_typing(page: Page):
    PLACEHOLDER = "Який гурток шукаєте?"
    TEXT = "A"
    search_component = HomePage(page).advanced_search_header_component

    (expect(search_component.selection_search_input_field_placeholder,
            message="Placeholder in the search field should have text" + PLACEHOLDER)
     .to_have_text(PLACEHOLDER))

    search_component.set_text_selection_search_input_field(TEXT)

    (expect(search_component.selection_search_input_field_placeholder,
            message="Placeholder in the search field should not be visible")
     .not_to_be_visible())
    (expect(search_component.selection_search_input_field,
            message="Search field should have text" + TEXT)
     .to_have_value(TEXT))

    search_component.selection_search_input_field.clear()

    (expect(search_component.selection_search_input_field_placeholder,
            message="Placeholder in the search field should have text" + PLACEHOLDER)
     .to_have_text(PLACEHOLDER))
