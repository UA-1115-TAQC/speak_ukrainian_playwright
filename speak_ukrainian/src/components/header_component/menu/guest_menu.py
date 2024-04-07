from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class GuestMenu(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._registration = None
        self._login = None
        self.login_form = None
        self.register_form = None

    def registration(self) -> Locator:
        if self._registration is None:
            self._registration = self.locator.locator("li.register")
        return self._registration

    def login(self) -> Locator:
        if self._login is None:
            self._login = self.locator.locator("li.login")
        return self._login
