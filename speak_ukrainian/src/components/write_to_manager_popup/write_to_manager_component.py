from playwright._impl._locator import Locator
from typing import Self

from speak_ukrainian.src.base import BasePopUp


class WriteToManagerPopUp(BasePopUp):

    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._submit_button = None
        self._add_comment_input = None

    @property
    def add_comment_element(self) -> Locator:
        self._add_comment_input = self.locator.get_by_placeholder("Додайте опис")
        return self._add_comment_input

    def add_comment_input(self, comment: str) -> Self:
        return self.add_comment_element.fill(comment)

    @property
    def submit_button(self) -> Locator:
        if self._submit_button is None:
            self._submit_button = self.locator.get_by_role("button", name="Надіслати")
            return self._submit_button

    def click_on_submit_button(self) -> Self:
        self.submit_button.click()
        return self
