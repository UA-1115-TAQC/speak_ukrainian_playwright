import pytest
from playwright.sync_api import expect
from speak_ukrainian.src.pages.home_page import HomePage

invalid_name_data = [
    ('AfBbCcDdEeFfGgHhIiJjKkLlMmNn', 'Ім\'я не може містити більше, ніж 25 символів'),
    #('AfBbCcDdEeFfGgHhIiJjKkLlMm', 'Ім\'я не може містити більше, ніж 25 символів'),
    #('!@#$%^&,', 'Ім\'я не може містити спеціальні символи'),
    #('1234', 'Ім\'я не може містити цифри'),
    #('-Name', 'Ім\'я повинно починатися та закінчуватися літерою'),
    #(' Name', 'Ім\'я не може містити спеціальні символи'),
    #('\'Name', 'Ім\'я повинно починатися та закінчуватися літерою'),
    #('Name-', 'Ім\'я повинно починатися та закінчуватися літерою'),
    #('Name ', 'Ім\'я не може містити спеціальні символи'),
    #('Name\'', 'Ім\'я повинно починатися та закінчуватися літерою'),
    #('', 'Введіть Ваше ім\'я')

]


@pytest.mark.parametrize("invalid_name, expected_error_msg", invalid_name_data)
def test_edit_name_filed_with_invalid_data(page_with_user: HomePage, invalid_name, expected_error_msg):
    profile_pop_up = (page_with_user.header.open_user_menu
                      .open_profile_page
                      .click_edit_profile_button())
    name_field = (profile_pop_up
                  .first_name_element)
    name_field.set_input_value(invalid_name)

    (expect(name_field.error_messages_list, f'\'{expected_error_msg}\' should be displayed')
     .to_have_text(expected_error_msg))

    (expect(profile_pop_up.submit_button, 'Submit button should be disabled')
     .to_be_disabled(timeout=500))
