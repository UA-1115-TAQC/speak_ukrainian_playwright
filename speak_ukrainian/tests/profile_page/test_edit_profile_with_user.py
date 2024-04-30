import allure
import pytest
from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.home_page import HomePage

invalid_name_data = [
    ('AfBbCcDdEeFfGgHhIiJjKkLlMmNn', 'Ім\'я не може містити більше, ніж 25 символів'),
    ('AfBbCcDdEeFfGgHhIiJjKkLlMm', 'Ім\'я не може містити більше, ніж 25 символів'),
    ('!@#$%^&,', 'Ім\'я не може містити спеціальні символи'),
    ('1234', 'Ім\'я не може містити цифри'),
    ('-Name', 'Ім\'я повинно починатися та закінчуватися літерою'),
    (' Name', 'Ім\'я не може містити спеціальні символи'),
    ('\'Name', 'Ім\'я повинно починатися та закінчуватися літерою'),
    ('Name-', 'Ім\'я повинно починатися та закінчуватися літерою'),
    ('Name ', 'Ім\'я не може містити спеціальні символи'),
    ('Name\'', 'Ім\'я повинно починатися та закінчуватися літерою'),
    ('', 'Введіть Ваше ім\'я')
]


@allure.issue('TUA-328')
@allure.description('Verify that error messages are shown'
                    ' and \'Зберегти зміни\' button becomes disabled'
                    ' while entering invalid data into the \'Ім\'я\' field as \'Відвідувач\'')
@allure.label("owner", "Olena Stankevych")
@pytest.mark.parametrize("invalid_name, expected_error_msg", invalid_name_data)
def test_edit_name_filed_with_invalid_data(page_with_user: HomePage, invalid_name, expected_error_msg):
    profile_pop_up = (page_with_user.header.open_user_menu
                      .open_profile_page
                      .click_edit_profile_button())
    name_field = (profile_pop_up
                  .first_name_element)
    name_field.set_input_value(invalid_name)

    (expect(name_field.error_messages_list[0], f'\'{expected_error_msg}\' should be displayed')
     .to_have_text(expected_error_msg, timeout=300))

    (expect(profile_pop_up.submit_button, 'Submit button should be disabled')
     .to_be_disabled(timeout=300))


@allure.issue('TUA-866')
@allure.description('Verify that the user can see ''Завантажити фото\' text link'
                    ' under the \'Фото\' link and tooltip message appears')
@allure.label("owner", "Olena Stankevych")
def test_verify_photo_link_visible(page_with_user: HomePage):
    expected_message = ("Приймас зображення формату JPG / PNG"
                        " із мінімальною роздільною здатністю 200x200 пікселів"
                        " та максимальним розміром файлу 5МВ")
    profile_pop_up = (page_with_user.header
                      .open_user_menu
                      .open_profile_page
                      .click_edit_profile_button())

    (expect(profile_pop_up.photo_title, '\'Фото\' link should be visible')
     .to_be_visible())

    (expect(profile_pop_up.uploaded_photo_element, '\'Завантажити фото\' link should be visible')
     .to_be_visible())

    (expect(profile_pop_up.tooltip_form(), f'\'{expected_message}\' should be visible')
     .to_have_text(expected_message))
