import pytest
from playwright.sync_api import expect
from playwright._impl._page import Page

from speak_ukrainian.src.components.header_component.header_component import HeaderComponent

from speak_ukrainian.tests.conftest import page_with_manager


invalid_data = [
    ("AfBbCcDdEeFfGgHhIiJjKkLlMmNn", "Ім'я не може містити більше, ніж 25 символів"),
    ("AfBbCcDdEeFfGgHhIiJjKkLlMm", "Ім'я не може містити більше, ніж 25 символів"),
    ("!@#$%^&,", "Ім'я не може містити спеціальні символи"),
    ("1234", "Ім'я не може містити цифри"),
    ("-Name", "Ім'я повинно починатися та закінчуватися літерою"),
    ("< Name>", "Ім'я не може містити спеціальні символи"),
    ("'Name", "Ім'я повинно починатися та закінчуватися літерою"),
    ("Name-", "Ім'я повинно починатися та закінчуватися літерою"),
    ("<Name >", "Ім'я не може містити спеціальні символи"),
    ("Name'", "Ім'я повинно починатися та закінчуватися літерою")
    ]


@pytest.mark.parametrize("invalid_first_name,expected_error_message", invalid_data)
def test_first_name_element_invalid_data(page_with_manager: Page, page, invalid_first_name, expected_error_message):
    edit_user = (HeaderComponent(page.get_by_role("banner"))
                 .open_user_menu
                 .open_profile_page
                 .click_edit_profile_button())
    (edit_user.first_name_element.set_input_value(invalid_first_name))

    (expect(edit_user.first_name_element.error_messages_list[0], f'\'{expected_error_message}\' should be displayed')
     .to_have_text(expected_error_message, timeout=300))

    (expect(edit_user.submit_button, 'Submit button should be disabled').to_be_disabled(timeout=100))

