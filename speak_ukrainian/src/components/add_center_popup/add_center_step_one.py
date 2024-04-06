from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from speak_ukrainian.src.elements.input_with_icons_and_errors import InputWithInfoValidationIconsAndErrors


class AddCenterStepOne(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._center_name_title = None
        self._locations_title = None
        self._next_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.modal-title")
        return self._popup_title

    @property
    def center_name_title(self) -> Locator:
        if self._center_name_title is None:
            self._center_name_title = self.locator.get_by_text("Назва центру", exact=True)
        return self._center_name_title

    @property
    def name_input_element(self) -> InputWithInfoValidationIconsAndErrors:
        return InputWithInfoValidationIconsAndErrors(self.locator.locator("div.ant-form-item-row")
                                                     .filter(has=self.locator.page.locator("#basic_name")))

    def locations_title(self) -> Locator:
        if self._locations_title is None:
            self._locations_title = self.locator.get_by_text("Локації", exact=True)
        return self._locations_title

    @property
    def add_location_button(self) -> Locator:
        return self.locator.locator("button.add-location-btn")

    def click_add_location_button(self) -> AddLocationPopUp:
        self.add_location_button.click()
        return AddLocationPopUp(self.locator.page.locator("div.modal-add-club"))

    @property
    def location_error_message(self) -> Locator:
        return self.locator.locator("#basic_locations_help")

    @property
    def locations_list(self) -> list[Locator]:
        return self.locator.locator("#basic_locations div.checkbox-item label").all()

    def get_locations_list_names(self) -> list[str]:
        return [location.text_content() for location in self.locations_list]

    @property
    def checked_locations_list(self) -> list[Locator]:
        return [location for location in self.locations_list if location.locator("input").is_checked()]

    def get_checked_locations_list_names(self) -> list[str]:
        return [location.text_content() for location in self.checked_locations_list]

    def click_location_checkbox_by_name(self, name: str) -> Self:
        for location in self.locations_list:
            print(location.text_content())
            if name in location.text_content():
                location.click()
        return self

    def click_location_checkbox_by_index(self, index: int) -> Self:
        self.locations_list[index].click()
        return self

    @property
    def next_step_button(self) -> Locator:
        if self._next_step_button is None:
            self._next_step_button = self.locator.get_by_role("button", name="Наступний крок")
        return self._next_step_button

    def click_next_step_button(self) -> None:
        self.next_step_button.click()
