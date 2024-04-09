from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class PopUpStep(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._step_title = None

    @property
    def step_title(self) -> Locator:
        if self._step_title is None:
            self._step_title = self.locator.locator("div.ant-steps-item-title")
        return self._step_title

    @property
    def step_icon(self) -> Locator:
        return self.locator.locator("div.ant-steps-item-icon")

    @property
    def step_success_icon(self) -> Locator:
        return self.locator.locator("div.ant-steps-finish-icon")
