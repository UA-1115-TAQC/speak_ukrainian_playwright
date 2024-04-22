from speak_ukrainian.src.web.pages.home_page import HomePage
from playwright.sync_api import expect
import pytest


# TUA-312
def test_display_add_club_popup(page_with_admin):
    add_club_popup = page_with_admin.header.click_add_club_button()
    expect(add_club_popup.locator).to_be_visible()


# TUA-931
valid_club_names = ["0123456789",
                    "фЙїqfGJHdsmnФІля",
                    "!@#$%^&*()_{:\"}]'",
                    "%;?*(?:фЙїqfG123456789",
                    "1&hЦ*",
                    "123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ",
                    ]


@pytest.mark.parametrize("valid_name", valid_club_names)
def test_valid_club_name(page_with_admin, valid_name):
    add_club_popup = page_with_admin.header.click_add_club_button()
    step_one = add_club_popup.step_one_container

    step_one.name_input_element.set_input_value(valid_name)
    expect(step_one.name_input_element.validation_circle_icon).to_have_css("color", "rgb(82, 196, 26)")

    step_one.name_input_element.clear_input()
    expect(step_one.name_input_element.validation_circle_icon).to_have_css("color", "rgb(255, 77, 79)")
    expect(step_one.name_input_element.error_messages_list[0]).to_have_text("Введіть назву гуртка")

