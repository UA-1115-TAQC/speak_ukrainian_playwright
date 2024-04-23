import allure
from speak_ukrainian.src.web.pages.home_page import HomePage
from playwright.sync_api import expect


@allure.issue("TUA-876")
@allure.description("[Registration] Verify that the user is redirected to the main page after canceling the registration process")
def test_redirection_after_registration_cancelled(page):
    current_page = HomePage(page).header.click_news_button()
    start_url = current_page.page.url

    registration_popup = current_page.header.open_guest_menu.open_register_form
    registration_popup.firstname_input_element.set_input_value("Qwerty")
    registration_popup.lastname_input_element.set_input_value("Qwerty")
    registration_popup.phone_input_element.set_input_value("0123456789")
    registration_popup.email_input_element.set_input_value("qwerty@email.com")
    registration_popup.click_close_button()

    expect(page).to_have_url(start_url)

