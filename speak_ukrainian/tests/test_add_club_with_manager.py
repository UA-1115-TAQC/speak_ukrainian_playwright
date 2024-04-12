import pytest
from playwright.sync_api import expect
from speak_ukrainian.src.pages.home_page import HomePage

invalid_name_data = [
    ('a' + ('a' * 100), 'Min: 5 characters, Max: 100 characters.'),
    ('name', 'Min: 5 characters, Max: 100 characters.')
]


@pytest.mark.parametrize("invalid_name, expected_error_msg", invalid_name_data)
def test_tip_about_amount_characters_in_name_field(page_with_manager: HomePage, invalid_name, expected_error_msg):
    name_field = (page_with_manager.header
                  .click_add_club_button()
                  .step_one_container
                  .name_input_element)
    name_field.set_input_value(invalid_name)
    (expect(name_field.error_messages_list[0],
            f'Message \'{expected_error_msg}\' should be visible')
     .to_have_text('Min: 5 characters, Max: 100 characters.', timeout=100))
