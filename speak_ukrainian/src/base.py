from playwright._impl._locator import Locator


class BasePage:
    def __init__(self, page):
        self.page = page


class BaseComponent:
    def __init__(self, locator):
        self.locator = locator


class BasePopUp(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._close_button = None

    def is_open(self) -> bool:
        return self.locator.is_visible()

    @property
    def close_button(self) -> Locator:
        if self._close_button is None:
            self._close_button = self.locator.get_by_label("Close", exact=True)
        return self._close_button

    def click_close_button(self) -> None:
        self.close_button.click()
