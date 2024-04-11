import time

from playwright.sync_api import expect
from playwright._impl._page import Page

from speak_ukrainian.src.components.header_component.header_component import HeaderComponent

from speak_ukrainian.tests.conftest import page_with_manager


def test_first_name_element_invalid_data(page_with_manager: Page, page):
    edit_user = (HeaderComponent(page.get_by_role("banner"))
                                .open_user_menu
                                .open_profile_page
                                .click_edit_profile_button())
    (edit_user.first_name_element
                                 .clear_input()
                                 .set_input_value("AfBbCcDdEeFfGgHhIiJjKkLlMmNn"))

    expect(edit_user.submit_button).to_be_disabled()


