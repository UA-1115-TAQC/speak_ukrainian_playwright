from typing import Self
from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class Dropdown(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

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

    def visible_items_list(self) -> list[Locator]:
        return self.locator.page.locator("div.rc-virtual-list div.ant-select-item.ant-select-item-option").all()

    def scroll_to_top(self):
        while True:
            current_first_item = self.visible_items_list()[0]
            current_first_item.scroll_into_view_if_needed()
            if current_first_item.text_content() == self.visible_items_list()[0].text_content():
                return

    def select_item(self, item_name) -> Self:
        self.scroll_to_top()
        while True:
            for item in self.visible_items_list():
                if item.text_content() == item_name:
                    item.click()
                    return self
            current_last_element = self.visible_items_list()[-1]
            current_last_element.scroll_into_view_if_needed()
            if current_last_element.text_content() == self.visible_items_list()[-1].text_content():
                break
        return self
