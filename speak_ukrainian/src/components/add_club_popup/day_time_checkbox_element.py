from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class DayTimeCheckboxElement(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def checkbox(self) -> Locator:
        return self.locator.get_by_role("checkbox")

    def click_on_checkbox(self) -> Self:
        self.checkbox_title.click()
        return self

    @property
    def checkbox_title(self) -> Locator:
        return self.locator.locator("label.ant-checkbox-wrapper")

    @property
    def clock_icon(self) -> Locator:
        return self.locator.get_by_label("clock-circle")

    @property
    def time_from_input(self) -> Locator:
        return self.locator.get_by_placeholder("HH:mm", exact=True).first

    def set_time_from_input(self, value: str) -> Self:
        self.wait_to_be_visible(self.time_from_input).fill(value)
        self.click_time_picker_button()
        return self

    @property
    def hours_picker_list(self) -> list[Locator]:
        return self.time_picker_container.locator("ul.ant-picker-time-panel-column").first.locator("li").all()

    def hours_text_picker_list(self) -> list[str]:
        return [item.text_content() for item in self.hours_picker_list]

    @property
    def minutes_picker_list(self) -> list[Locator]:
        return self.time_picker_container.locator("ul.ant-picker-time-panel-column").last.locator("li").all()

    def minutes_text_picker_list(self) -> list[str]:
        return [item.text_content() for item in self.minutes_picker_list]

    @property
    def time_to_input(self) -> Locator:
        return self.locator.get_by_placeholder("HH:mm", exact=True).last

    def set_time_to_input(self, value: str) -> Self:
        self.wait_to_be_visible(self.time_to_input).fill(value)
        self.click_time_picker_button()
        return self

    @property
    def time_picker_button(self) -> Locator:
        return self.locator.get_by_role("button", name="OK")

    @property
    def time_picker_container(self) -> Locator:
        return self.locator.locator("div.ant-picker-time-range-wrapper")

    def click_time_picker_button(self) -> Self:
        self.time_picker_button.click()
        return self
