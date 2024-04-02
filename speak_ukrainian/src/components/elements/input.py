from typing import Self


class Input:
    def __init__(self, page):
        self.page = page

    def input(self):
        return self.page.locator("[class*='input']")

    def set_input_value(self, input_value, selector_name) -> None:
        placeholder = self.input().locator(selector_name).first
        placeholder.fill(input_value)

    def get_input_value(self, selector_name) -> str:
        input_element = self.input().locator(selector_name).first
        return input_element.get_attribute("value")

    def clear_input(self, selector_name) -> Self:
        self.input().locator(selector_name).click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.page.keyboard.down("Meta")
        self.page.keyboard.press("a")
        self.page.keyboard.up("Meta")
        self.page.keyboard.press("Backspace")
        return self
