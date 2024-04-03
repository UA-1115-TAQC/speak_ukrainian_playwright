from typing import Self

from playwright.sync_api import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.elements.input_with_icon_element import InputWithIconElement


class LoginPopUpComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def login_popup_title(self) -> Locator:
        return self.locator.get_by_text("Вхід", exact=True)

    @property
    def authorization_by_google(self) -> Locator:
        return self.locator.locator("a[href*=google]")

    @property
    def authorization_by_facebook(self) -> Locator:
        return self.locator.locator("a[href*=facebook]")

    @property
    def google_icon(self) -> Locator:
        return self.locator.locator("img.logo[src*='google.png']")

    @property
    def facebook_icon(self) -> Locator:
        return self.locator.locator("img.logo[src*='facebook.png']")

    @property
    def or_tittle_text(self) -> Locator:
        return self.locator.get_by_text("або", exact=True)

    @property
    def email_title(self) -> Locator:
        return self.locator.get_by_text("Емейл", exact=True)

    @property
    def password_title(self) -> Locator:
        return self.locator.get_by_text("Пароль", exact=True)

    @property
    def sing_in_button(self) -> Locator:
        # sign_in_button = self.locator.get_by_role("button", name="Увійти")
        return self.locator.locator("button[class*=login-button]")

    def click_sign_in_button(self) -> None:
        self.sing_in_button.click()

    @property
    def restore_password_button(self) -> Locator:
        # restore_password_button = self.locator.get_by_role("link", name="Забули пароль?")
        return self.locator.locator("a.restore-password-button")

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
        return self.email_input_element.set_input_value(email)

    def enter_password(self, password: str) -> Self:
        return self.password_input_element.set_input_value(password)


class RestorationPasswordPopup(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def restoration_password_title(self) -> Locator:
        return self.locator.get_by_text("Відновлення", exact=True)

    @property
    def close_button(self) -> Locator:
        return self.locator.get_by_label("Close").last

    @property
    def restore_email_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.locator.locator("div.login-input").last)

    def enter_email(self, email: str) -> Self:
        return self.restore_email_input_element.set_input_value(email)

    def click_close_restoration_popup(self) -> LoginPopUpComponent:
        self.close_button.click()
        return LoginPopUpComponent(self.locator.locator("div.ant-modal-content").first)

    @property
    def restore_button(self) -> Locator:
        return self.locator.get_by_role("button", name="Відновити")

    def click_restore_button(self) -> None:
        self.restore_button.click()
