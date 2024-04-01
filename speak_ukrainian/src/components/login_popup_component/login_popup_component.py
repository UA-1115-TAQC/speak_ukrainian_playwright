from playwright.sync_api import Locator

from speak_ukrainian.src.base import BasePage, BaseComponent
from speak_ukrainian.src.components.elements.input import Input


class LoginPopUpComponent(BaseComponent, Input):
    def __init__(self, locator):
        super().__init__(locator)
        self._login_popup_title = None
        self._google_icon = None
        self._facebook_icon = None
        self._authorization_by_google = None
        self._authorization_by_facebook = None
        self._label_or_title = None
        self._email_title = None
        self._password_title = None
        self._sign_in_button = None
        self._restore_password_button = None
        self._restore_password_popup = None
        self._email_input = None
        self._password_input = None

    @property
    def login_popup_title(self) -> Locator:
        if self._login_popup_title is None:
            self._login_popup_title = self.locator.get_by_text("Вхід")
        return self._login_popup_title

    @property
    def authorization_by_google(self) -> Locator:
        if self._authorization_by_google is None:
            self._authorization_by_google = self.locator.get_by_role("link", name="Logo")
        return self._authorization_by_google

    @property
    def authorization_by_facebook(self) -> Locator:
        if self._authorization_by_facebook is None:
            self._authorization_by_facebook = self.locator.get_by_role("link", name="Logo").nth(1)
        return self._authorization_by_facebook

    @property
    def google_icon(self) -> Locator:
        if self._google_icon is None:
            self._google_icon = self.locator.query_selector("img.logo[src*='google.png'][alt='Logo']")
        return self._google_icon

    @property
    def facebook_icon(self) -> Locator:
        if self._facebook_icon is None:
            self._facebook_icon = self.locator.query_selector("img.logo[src*='facebook.png'][alt='Logo']")
        return self._facebook_icon

    @property
    def or_tittle_text(self) -> Locator:
        if self._label_or_title is None:
            self._label_or_title = self.locator.get_by_text("або")
        return self._label_or_title

    @property
    def email_title(self) -> Locator:
        if self._email_title is None:
            self._email_title = self.locator.get_by_text("Емейл")
        return self._email_title

    @property
    def password_title(self) -> Locator:
        if self._password_title is None:
            self._password_title = self.locator.get_by_text("Пароль", exact=True)
        return self._password_title

    def click_sign_in_button(self) -> None:
        if self._sign_in_button is None:
            self._sign_in_button = self.locator.get_by_role("button", name="Увійти")
        self._sign_in_button.click()

    def open_restoration_password_popup(self) -> None:  # TODO (add return value)
        if self._restore_password_button is None:
            self._restore_password_button = self.locator.get_by_role("link", name="Забули пароль?")
        self._restore_password_button.click()

    def enter_email(self, email: str) -> None:
        self.set_input_value(email, "#basic_email")

    def enter_password(self, password: str) -> None:
        self.set_input_value(password, "#basic_password")


