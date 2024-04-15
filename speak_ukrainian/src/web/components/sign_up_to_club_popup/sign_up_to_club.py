from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BasePopUp
from speak_ukrainian.src.web.components.sign_up_to_club_popup.add_child import AddChildPopUp


class SignUpToClub(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._add_child_button = None
        self.add_comment = None
        self.submit_button = None

    @property
    def add_child_button(self) -> Locator:
        if self._add_child_button is None:
            self._add_child_button = self.locator.get_by_role("button", name="plus Додати дитину")
            return self.add_child_button

    def click_add_child_button(self) -> AddChildPopUp:
        self.add_child_button.click()
        return AddChildPopUp(self.locator)


