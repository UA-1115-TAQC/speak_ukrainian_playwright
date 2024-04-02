from typing import Self

from playwright.sync_api import Locator

from speak_ukrainian.src.base import BaseComponent


class Input(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def input(self) -> Locator:
        return self.locator.locator("input")

    def set_input_value(self, input_value) -> None:
        self.input.fill(input_value)

    def get_input_value(self) -> Self:
        self.input.input_value()
        return self

    def clear_input(self) -> Self:
        self.input.clear()
        return self
