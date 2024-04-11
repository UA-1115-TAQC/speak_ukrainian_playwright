from playwright.sync_api import Locator

from speak_ukrainian.src.elements.input import Input


class InputWithIconElement(Input):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def static_icon(self) -> Locator:
        return self.locator.get_by_role("img", name="mail")

    @property
    def validation_circle_icon(self) -> Locator:
        close_circle_locator = self.locator.get_by_role("img", name="close-circle")
        check_circle_locator = self.locator.get_by_role("img", name="check-circle")
        return close_circle_locator.or_(check_circle_locator)

    @property
    def password_visibility_icon(self) -> Locator:
        eye = self.locator.get_by_role("img", name="eye")
        eye_invisible = self.locator.get_by_role("img", name="eye-invisible")
        return eye.or_(eye_invisible)

    @property
    def error_messages_list(self) -> list[Locator]:
        return self.locator.locator("div.ant-form-item-explain-error").all()

    def get_error_messages_text_list(self) -> list[str]:
        return [error.text_content() for error in self.error_messages_list]
