import time
from typing import Self
from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.web.base import BaseComponent


class Dropdown(BaseComponent):
    def __init__(self, locator: Locator, dropdown_id: str):
        super().__init__(locator)
        self._dropdown_id = dropdown_id

    @property
    def dropdown_input(self) -> Locator:
        return self.locator.locator("input")

    def click_dropdown(self) -> Self:
        self.locator.click()
        return self

    @property
    def placeholder(self) -> Locator:
        return self.locator.locator("span.ant-select-selection-placeholder")

    @property
    def arrow_icon(self) -> Locator:
        return self.locator.get_by_label("down", exact=True)

    @property
    def selected_item(self) -> Locator:
        return self.locator.locator("span.ant-select-selection-item")

    @property
    def visible_items_list(self) -> list[Locator]:
        return (self.locator.page.locator("div").filter(has=self.locator.page.locator("#" + self._dropdown_id))
                                 .locator("div.rc-virtual-list div.ant-select-item.ant-select-item-option").all())

    def scroll_to_top(self):
        while True:
            current_first_element = self.wait_to_be_visible(self.visible_items_list[0])
            current_first_element_text = current_first_element.text_content()
            current_first_element.scroll_into_view_if_needed()
            time.sleep(0.1)
            if current_first_element_text == self.wait_to_be_visible(self.visible_items_list[0]).text_content():
                return

    def select_item(self, item_name) -> Self:
        self.scroll_to_top()
        while True:
            for item in self.visible_items_list:
                if item_name in item.text_content():
                    expect(item).to_be_visible()
                    item.scroll_into_view_if_needed()
                    item.click()
                    return self
            current_last_element = self.wait_to_be_visible(self.visible_items_list[-1])
            current_last_element_text = current_last_element.text_content()
            current_last_element.scroll_into_view_if_needed()
            time.sleep(0.1)
            if current_last_element_text == self.wait_to_be_visible(self.visible_items_list[-1]).text_content():
                break
        return self


class DropdownWithIconError(Dropdown):
    def __init__(self, locator: Locator, dropdown_id: str):
        super().__init__(locator, dropdown_id)

    @property
    def validation_circle_icon(self):
        check_circle = self.locator.get_by_label("check-circle")
        close_circle = self.locator.get_by_label("close-circle")
        expect(check_circle.or_(close_circle)).to_be_visible()
        return check_circle if check_circle.is_visible() else close_circle

    @property
    def error_message(self) -> Locator:
        return self.locator.locator("div.ant-form-item-explain-error")
