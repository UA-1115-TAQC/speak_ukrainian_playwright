from playwright._impl._locator import Locator
from playwright._impl._sync_base import Self

from speak_ukrainian.src.base import BasePopUp


class AnswerToCommentPopUpComponent(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._add_comment = None
        self._submit_button = None

    @property
    def submit_button(self) -> Locator:
        self._add_comment = self.locator.get_by_role("button", name="Надіслати")
        return self._submit_button

    def click_on_submit_button(self) -> Self:
        self.submit_button.click()
        return self

    @property
    def add_comment(self) -> Locator:
        self._add_comment = self.locator.get_by_placeholder("Додайте коментар")
        return self._add_comment

    def click_on_complain_tab(self) -> Self:
        self.add_comment.click()
        return self
