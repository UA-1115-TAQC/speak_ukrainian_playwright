from playwright._impl._locator import Locator
from typing import Self

from speak_ukrainian.src.web.base import BasePopUp
from speak_ukrainian.src.web.components.sign_up_to_club_popup.add_child import AddChildPopUp


class SignUpToClub(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._add_child_button = None
        self._add_comment = None
        self._submit_button = None

    @property
    def add_child_button(self) -> Locator:
        if self._add_child_button is None:
            self._add_child_button = self.locator.get_by_role("button", name="plus Додати дитину")
            return self.add_child_button

    def click_add_child_button(self) -> AddChildPopUp:
        self.add_child_button.click()
        return AddChildPopUp(self.locator)

    @property
    def children_list(self) -> list[Locator]:
        return self.locator.locator('div[class*="SignUpForClub_customCheckbox"]').all()

    def click_child_checkbox_by_index(self, index: int) -> Self:
        self.children_list[index].click()
        return self

    @property
    def comment_input_element(self) -> Locator:
        self._add_comment = self.locator.get_by_placeholder("Додати коментар")
        return self._add_comment

    def fill_comment_input(self, comment: str) -> Self:
        return self.comment_input_element.fill(comment)

    @property
    def submit_button_element(self) -> Locator:
        self._submit_button = self.locator.get_by_role("button", name="Записати", exact=True)
        return self._submit_button

    def click_submit_button(self) -> Self:
        self.submit_button_element.click()
        return self
