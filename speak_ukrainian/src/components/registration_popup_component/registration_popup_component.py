from playwright.sync_api import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.elements.input_with_icon_element import InputWithIconElement


class RegistrationPopUpComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._registration_popup_title = None
        self._google_icon = None
        self._facebook_icon = None
        self._user_type_button = None
        self._manager_type_button = None
        self._lastname_input = None
        self._firstname_input = None
        self._phone_input = None
        self._email_input = None
        self._password_input = None
        self._password_confirmation_input = None
        self._registration_button = None

    @property
    def registration_popup_title(self) -> Locator:
        if self._registration_popup_title is None:
            self._registration_popup_title = self.locator.get_by_text("Реєстрація", exact=True)
        return self._registration_popup_title

    @property
    def google_icon(self) -> Locator:
        if self._google_icon is None:
            self._google_icon = self.locator.locator('a[href*="google"]')
        return self._google_icon

    @property
    def facebook_icon(self) -> Locator:
        if self._facebook_icon is None:
            self._facebook_icon = self.locator.locator('a[href*="facebook"]')
        return self._facebook_icon

    @property
    def user_type_button(self) -> Locator:
        if self._user_type_button is None:
            self._user_type_button = self.locator.locator("label:has(input[value=\"ROLE_USER\"])")
        return self._user_type_button

    @property
    def manager_type_button(self) -> Locator:
        if self._manager_type_button is None:
            self._manager_type_button = self.locator.locator("label:has(input[value=\"ROLE_MANAGER\"])")
        return self._manager_type_button

    @property
    def lastname_input_element(self) -> InputWithIconElement:
        if self._lastname_input is None:
            self._lastname_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").first)
        return self._lastname_input

    @property
    def firstname_input_element(self) -> InputWithIconElement:
        if self._firstname_input is None:
            self._firstname_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").nth(1))
        return self._firstname_input

    @property
    def phone_input_element(self) -> InputWithIconElement:
        if self._phone_input is None:
            self._phone_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").nth(2))
        return self._phone_input

    @property
    def email_input_element(self) -> InputWithIconElement:
        if self._email_input is None:
            self._email_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").nth(3))
        return self._email_input

    @property
    def password_input_element(self) -> InputWithIconElement:
        if self._password_input is None:
            self._password_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").nth(4))
        return self._password_input

    @property
    def password_confirmation_input_element(self) -> InputWithIconElement:
        if self._password_confirmation_input is None:
            self._password_confirmation_input = InputWithIconElement(self.locator.locator("div.ant-form-item.registration-input").nth(5))
        return self._password_confirmation_input

    @property
    def registration_button(self) -> Locator:
        # sign_in_button = self.locator.get_by_role("button", name="Увійти")
        if self._registration_button is None:
            self._registration_button = self.locator.locator("button.registration-button")
        return self._registration_button

    def register(self) -> None:
        self.registration_button.click()
