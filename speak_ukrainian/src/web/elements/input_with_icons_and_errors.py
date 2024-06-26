from typing import Self

from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.web.elements.input import Input


class InputValidationIconAndErrors(Input):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def validation_circle_icon(self):
        check_circle = self.locator.get_by_label("check-circle")
        close_circle = self.locator.get_by_label("close-circle")
        expect(check_circle.or_(close_circle)).to_be_visible()
        return check_circle if check_circle.is_visible() else close_circle

    @property
    def error_messages_list(self) -> list[Locator]:
        return self.locator.locator("div.ant-form-item-explain-error").all()

    def get_error_messages_text_list(self) -> list[str]:
        return [error.text_content() for error in self.error_messages_list]


class InputValidationStaticIconsAndErrors(InputValidationIconAndErrors):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def static_icon(self):
        return self.locator.locator("span.ant-input-suffix div.icon")


class InputInfoValidationIconsAndErrors(InputValidationIconAndErrors):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def info_icon(self):
        return self.locator.get_by_label("info-circle", exact=True)

    def click_info_icon(self) -> Self:
        self.info_icon.click()
        return self

    @property
    def info_icon_tooltip(self) -> Locator:
        return self.locator.page.get_by_role("tooltip", exact=True)

    def get_info_icon_tooltip_text(self) -> str:
        return self.info_icon_tooltip.text_content()


class InputLabelValidationIconAndErrors(InputValidationIconAndErrors):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def label(self):
        return self.locator.locator("div.ant-form-item-label > label")


class InputPasswordVisibilityIcon(InputValidationIconAndErrors):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def password_visibility_icon(self):
        return self.locator.locator("div.ant-input-password-icon")

    def click_on_password_visibility_icon(self):
        return self.password_visibility_icon.click()
