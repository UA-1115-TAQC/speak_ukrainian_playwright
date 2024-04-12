from typing import Self

from playwright.sync_api import Locator

from speak_ukrainian.src.base import BaseComponent, BasePage
from speak_ukrainian.src.elements.input_with_icon_element import InputWithIconElement
from speak_ukrainian.src.pages.home_page import HomePage


class LoginPopUpComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._login_popup_title = None
        self._google_icon = None
        self._facebook_icon = None
        self._authorization_by_google = None
        self._authorization_by_facebook = None
        self._label_or_title = None
        self._email_title = None
        self._password_title = None
        self._sing_in_button = None
        self._restore_password_button = None

    @property
    def login_popup_title(self) -> Locator:
        if self._login_popup_title is None:
            self._login_popup_title = self.locator.get_by_text("Вхід", exact=True)
        return self._login_popup_title

    @property
    def authorization_by_google(self) -> Locator:
        if self._authorization_by_google is None:
            self._authorization_by_google = self.locator.locator("a[href*=google]")
        return self._authorization_by_google

    @property
    def authorization_by_facebook(self) -> Locator:
        if self._authorization_by_facebook is None:
            self._authorization_by_facebook = self.locator.locator("a[href*=facebook]")
        return self._authorization_by_facebook

    @property
    def google_icon(self) -> Locator:
        if self._google_icon is None:
            self._google_icon = self.locator.locator("img.logo[src*='google.png']")
        return self._google_icon

    @property
    def facebook_icon(self) -> Locator:
        if self._facebook_icon is None:
            self._facebook_icon = self.locator.locator("img.logo[src*='facebook.png']")
        return self._facebook_icon

    @property
    def or_tittle_text(self) -> Locator:
        if self._label_or_title is None:
            self._label_or_title = self.locator.get_by_text("або", exact=True)
        return self._label_or_title

    @property
    def email_title(self) -> Locator:
        if self._email_title is None:
            self._email_title = self.locator.get_by_text("Емейл", exact=True)
        return self._email_title

    @property
    def password_title(self) -> Locator:
        if self._password_title is None:
            self._password_title = self.locator.get_by_text("Пароль", exact=True)
        return self._password_title

    @property
    def sing_in_button(self) -> Locator:
        if self._sing_in_button is None:
            self._sing_in_button = self.locator.locator("button[class*=login-button]")
        return self._sing_in_button

    @property
    def click_sign_in_button(self) -> HomePage:
        self.sing_in_button.click()
        return HomePage(self.locator.page)

    @property
    def restore_password_button(self) -> Locator:
        if self._restore_password_button is None:
            self._restore_password_button = self.locator.locator("a.restore-password-button")
        return self._restore_password_button

    @property
    def open_restoration_password_popup(self) -> 'RestorationPasswordPopup':
        self.restore_password_button.click()
        return RestorationPasswordPopup(self.locator.page.locator("div.modal-login").last)

    @property
    def email_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.locator.locator("div.login-input").first)

    @property
    def password_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.locator.locator("div.login-input").nth(1))

    def enter_email(self, email: str) -> Self:
        self.email_input_element.set_input_value(email)
        return self

    def enter_password(self, password: str) -> Self:
        self.password_input_element.set_input_value(password)
        return self


class RestorationPasswordPopup(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._restoration_password_title = None
        self._close_button = None
        self._restore_button = None

    @property
    def restoration_password_title(self) -> Locator:
        if self._restoration_password_title is None:
            self._restoration_password_title = self.locator.get_by_text("Відновлення", exact=True)
        return self._restoration_password_title

    @property
    def close_button(self) -> Locator:
        if self._close_button is None:
            self._close_button = self.locator.get_by_label("Close").last
        return self._close_button

    @property
    def restore_email_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.locator.locator("div.login-input").last)

    def enter_email(self, email: str) -> Self:
        self.restore_email_input_element.set_input_value(email)
        return self

    def click_close_restoration_popup(self) -> LoginPopUpComponent:
        self.close_button.click()
        return LoginPopUpComponent(self.locator.locator("div.ant-modal-content").first)

    @property
    def restore_button(self) -> Locator:
        if self._restore_button is None:
            self._restore_button = self.locator.get_by_role("button", name="Відновити")
        return self._restore_button

    def click_restore_button(self) -> None:
        self.restore_button.click()
