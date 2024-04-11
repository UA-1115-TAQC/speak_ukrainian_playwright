import allure
from playwright.sync_api import expect

from speak_ukrainian.src.pages.home_page import HomePage


@allure.issue("TUA-121")
@allure.description("Verify that a club without center is created if all parameters are filled with valid values")
def test_add_club_without_center(page_with_manager: HomePage):
    add_club_popup = page_with_manager.header.click_add_club_button()
    step_one = add_club_popup.step_one_container

    assert step_one.name_input_element.get_input_value() == ""

    categories_checkbox = step_one.categories_checkbox_list
    for category_checkbox in categories_checkbox:
        expect(category_checkbox).not_to_be_checked()

    assert step_one.min_age_input_element.get_input_value() == ""
    assert step_one.max_age_input_element.get_input_value() == ""
    assert step_one.center_dropdown_element.placeholder.text_content() == "Назва центру"

    step_one.name_input_element.set_input_value("Hip Hop")
    step_one.click_on_category_by_name("Танці, хореографія")
    step_one.min_age_input_element.set_input_value("6")
    step_one.max_age_input_element.set_input_value("30")

    step_two = step_one.click_next_step_button()
    step_two.popup_title.text_content()

    assert step_two.is_switch_button_checked() is False

    assert step_two.checked_work_days_list == []
