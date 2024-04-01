from speak_ukrainian.src.base import BasePage, BaseComponent
from speak_ukrainian.src.components.elements.input import Input


class LoginPopUpComponent(BaseComponent, Input):
    def __init__(self, locator):
        super().__init__(locator)

    # def __init__(self, page):
    #     super().__init__(page)

        self._login_popup_title = None
        self._google_icon = None
        self._facebook_icon = None
        self._authorization_by_google = None
        self._authorization_by_facebook = None
        self._label_or_title = None
        self._email_title = None
        self._password_title = None
        self._submit_button = None
        self._restore_password_button = None
        self._restore_password_popup = None
        self._email_input = None
        self._password_input = None

    def login_popup_title_text(self) -> str:
        if self._login_popup_title is None:
            self._login_popup_title = self.locator.get_by_text("Вхід").first
        return self._login_popup_title.first.text_content()

    def google_icon(self):
        return self.locator.get_by_role("link", name="Logo").first

    def facebook_icon(self):
        return self.locator.get_by_role("link", name="Logo").nth(1)

    def or_tittle_text(self) -> str:
        return self.page.locator.get_by_text("або").first.text_content()

    def enter_email(self, email: str) -> None:
        self.set_input_value(email, "#basic_email")

    def enter_password(self, password: str) -> None:
        self.set_input_value(password, "#basic_password")


