from playwright._impl._locator import Locator
from typing import Self

from speak_ukrainian.src.web.base import BasePopUp


class AddCommentPopUpComponent(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._complain_tab = None
        self._comment_tab = None
        self._add_comment = None
        self._submit_button = None
        self._rating = None

    @property
    def complain_tab(self) -> Locator:
        self._complain_tab = self.locator.get_by_role("tab", name="Скарга")
        return self._complain_tab

    def click_on_complain_tab(self) -> Self:
        self.complain_tab.click()
        return self

    @property
    def comment_tab(self) -> Locator:
        self._add_comment = self.locator.get_by_role("tab", name="Коментар")
        return self._comment_tab

    def click_on_comment_tab(self) -> Self:
        self.comment_tab.click()
        return self

    @property
    def add_comment(self) -> Locator:
        self._add_comment = self.locator.get_by_placeholder("Додайте коментар")
        return self._add_comment

    def fill_comment_input(self, comment: str) -> Self:
        self.add_comment.fill(comment)
        return self

    @property
    def submit_button(self) -> Locator:
        self._submit_button = self.locator.get_by_role("button", name="Надіслати")
        return self._submit_button

    def click_submit_button(self) -> Self:
        self.submit_button.click()
        return self

    @property
    def star_list(self) -> list[Locator]:
        return self.locator.get_by_role("radio", name="star star").all()

    def rate_the_club(self, rate: int) -> Self:
        for i in range(min(rate, len(self.star_list))):
            self.star_list[i].click()
        return self


