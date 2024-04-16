import allure
import pytest
from playwright.sync_api import expect
from playwright._impl._page import Page

from speak_ukrainian.src.web.components.header_component.header_component import HeaderComponent


invalid_data = [
    ("Михайло Михайлович Коцюбинський", "Прізвище не може містити більше, ніж 25 символів"),
    ("Тарас Григорович Шевченков", "Прізвище не може містити більше, ніж 25 символів"),
    ("#1Іван", ["Прізвище не може містити цифри", "Прізвище не може містити спеціальні символи"]),
    ("#1@Василь", ["Прізвище не може містити цифри", "Прізвище не може містити спеціальні символи"]),
    (" Ольга", "Прізвище повинно починатися і закінчуватися літерою"),
    ("K'", "Прізвище повинно починатися і закінчуватися літерою"),
    ("C- ", "Прізвище повинно починатися і закінчуватися літерою")
]


@allure.issue("TUA-13")
@allure.description("Verify that error messages are shown for entering invalid data for the 'Прізвище' field")
@pytest.mark.parametrize("data, expected_error_messages", invalid_data)
def test_registration_invalid_data_error_message_shown(page: Page, data: str, expected_error_messages: str):
    header = HeaderComponent(page.get_by_role('banner'))
    guest_menu = header.open_guest_menu
    registration = guest_menu.open_register_form

    registration.manager_type_button.click()
    last_name = registration.lastname_input_element.set_input_value(data)

    if isinstance(expected_error_messages, str):
        expected_error_messages = [expected_error_messages]

    for index, error_message in enumerate(expected_error_messages):
        (expect(last_name.error_messages_list[index],
                f"Should display next error message: {error_message}")
         .to_have_text(error_message))
        expect(registration.registration_button).to_be_disabled()

    registration.user_type_button.click()
    last_name = registration.lastname_input_element.set_input_value(data)

    for index, error_message in enumerate(expected_error_messages):
        (expect(last_name.error_messages_list[index],
                f"Should display next error message: {error_message}")
         .to_have_text(error_message))
        expect(registration.registration_button).to_be_disabled()
