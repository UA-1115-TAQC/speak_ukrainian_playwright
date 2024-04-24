import allure
import pytest
from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.home_page import HomePage

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


@allure.issue("TUA-835")
@allure.description("Verify that error messages are shown and 'Зберегти зміни' button "
                    "becomes disabled while entering invalid data into the 'Ім'я' field as 'Керівник'")
@pytest.mark.parametrize("invalid_first_name,expected_error_message", invalid_data)
def test_first_name_element_invalid_data(page_with_manager: HomePage, invalid_first_name, expected_error_message):
    edit_user = (page_with_manager.header
                      .open_user_menu
                      .open_profile_page
                      .click_edit_profile_button())
    (edit_user.first_name_element.set_input_value(invalid_first_name))

    (expect(edit_user.first_name_element.error_messages_list[0], f'\'{expected_error_message}\' should be displayed')
     .to_have_text(expected_error_message, timeout=300))

    (expect(edit_user.submit_button, 'Submit button should be disabled').to_be_disabled(timeout=100))


@allure.issue("TUA-867")
@allure.description("Verify that the user as 'Керівник' see 'Завантажити фото' text link "
                    "under the 'Фото' link and tooltip message appears")
def test_tooltip(page_with_manager: HomePage):
    edit_user = (page_with_manager.header
                      .open_user_menu
                      .open_profile_page
                      .click_edit_profile_button())

    expect(edit_user.tooltip_form(), f' The tooltip should be visible').to_be_visible()

    expected_tooltip_text = ("Приймас зображення формату JPG / PNG із мінімальною роздільною"
                             " здатністю 200x200 пікселів та максимальним розміром файлу 5МВ")

    (expect(edit_user.tooltip_form(), f'\'{expected_tooltip_text}\' should appeared')
     .to_have_text(expected_tooltip_text))

