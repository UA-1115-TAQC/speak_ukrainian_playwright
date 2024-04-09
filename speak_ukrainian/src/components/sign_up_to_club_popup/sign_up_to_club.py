from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class SignUpToClub(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self.add_child_button = None
        self.add_comment = None
        self.submit_button = None

    @property
    def add_child_button(self) -> Locator:
        if not self.add_child_button:
            self.add_child_button = (self.locator.get_by_role("button", name="plus Додати дитину"))
            return self.add_child_button
