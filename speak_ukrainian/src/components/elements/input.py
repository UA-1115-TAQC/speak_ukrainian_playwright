from typing import Self
from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class Input(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def input(self) -> Locator:
        return self.locator.locator("input")

    def get_input_value(self) -> Self:
        self.wait_to_be_visible(self.input).input_value()
        return self

    def set_input_value(self, value: str) -> Self:
        self.wait_to_be_visible(self.input).fill(value)
        return self

    def clear_input(self) -> Self:
        self.input.clear()
        return self
