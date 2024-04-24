import allure
import pytest
from playwright.sync_api import expect
from speak_ukrainian.src.web.pages.home_page import HomePage

invalid_name_data = [
    ('a' + ('a' * 100), 'Min: 5 characters, Max: 100 characters.'),
    ('name', 'Min: 5 characters, Max: 100 characters.')
]

invalid_location_name_data = [
    ("Ы, э, Ѩ, Ѭ,", "Це поле може містити тільки українські та англійські літери, цифри та спеціальні символи"),
    ("dfdg", "Назва локації закоротка"),
    ("vbyui1258/" * 9 + "nyrfvdoiu2587", "Назва локації задовга")
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


@allure.issue("TUA-249")
@allure.description("Verify error message for ‘Назва’ field of ‘Додати локацію’ pop-up when creating a club")
@pytest.mark.parametrize("location_name, error_message", invalid_location_name_data)
def test_error_messages_for_name_location_field(page_with_manager: HomePage, location_name, error_message):
    open_popup = (page_with_manager.header
                  .open_user_menu
                  .open_profile_page
                  .click_add_club_button())
    step_one = open_popup.step_one_container
    step_one.name_input_element.set_input_value("Abra Cadabra")
    (step_one.click_on_category_by_name("Художня студія, мистецтво, дизайн")
     .min_age_input_element.set_input_value("5"))
    step_one.max_age_input_element.set_input_value("10")
    step_two = step_one.click_next_step_button().click_add_location_button()
    location = step_two.name_input_element

    location.set_input_value(location_name)
    (expect(location.error_messages_list[0], f'Error messages \'{error_message} should be displayed')
     .to_have_text(error_message, timeout=50))
