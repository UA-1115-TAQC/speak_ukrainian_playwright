from dotenv import load_dotenv
import pytest
from speak_ukrainian.tests.conftest import page

load_dotenv()

class TestRegistrationCancellation():
    page()

    # TUA-876
    def test_redirection_after_registration_cancelled(self):
        header = self.homepage.header
        current_page = header.click_news_button()
        url = self.driver.current_url

        register_popup = header.click_profile_button().open_registration_form()
        register_popup.firstname_input_element.set_input_value("Qwerty")
        register_popup.lastname_input_element.set_input_value("Qwerty")
        register_popup.phone_input_element.set_input_value("0123456789")
        register_popup.email_input_element.set_input_value("qwerty@email.com")
        register_popup.click_close_button()

        new_url = self.driver.current_url
        self.assertEqual(url, new_url)