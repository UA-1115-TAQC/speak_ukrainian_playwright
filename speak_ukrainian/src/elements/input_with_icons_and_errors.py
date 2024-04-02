from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.elements.input import Input


class InputWithValidationIconAndErrors(Input):
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
        return [error.get_attribute("innerText") for error in self.error_messages_list]


class InputWithValidationStaticIconsAndErrors(InputWithValidationIconAndErrors):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def static_icon(self):
        return self.locator.locator("span.ant-input-suffix div.icon")
