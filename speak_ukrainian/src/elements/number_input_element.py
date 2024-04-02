from playwright._impl._locator import Locator

from speak_ukrainian.src.elements.input import Input


class NumberInput(Input):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def increase_button(self):
        return self.locator.get_by_label("increase value", exact=True)

    @property
    def decrease_button(self):
        return self.locator.get_by_label("decrease value", exact=True)

    @property
    def input_error(self):
        return self.locator.get_by_role("alert")
