from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.add_center_popup.club_checkbox_logo_name_element import ClubCheckboxLogoNameElement


class AddCenterStepFour(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._select_club_title = None
        self._previous_step_button = None
        self._complete_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.modal-title")
        return self._popup_title

    @property
    def select_club_title(self) -> Locator:
        if self._select_club_title is None:
            self._select_club_title = self.locator.get_by_text("Оберіть гурток", exact=True)
        return self._select_club_title

    @property
    def club_webelements_list(self) -> list[Locator]:
        return self.locator.locator("#clubs div.checkbox-item label").all()

    @property
    def club_checkbox_logo_names_list(self) -> list[ClubCheckboxLogoNameElement]:
        return [ClubCheckboxLogoNameElement(club) for club in self.club_webelements_list]

    def get_club_names_list(self) -> list[str]:
        return [club.club_name.text_content() for club in self.club_checkbox_logo_names_list]

    def click_on_club_checkbox_by_name(self, name: str) -> Self:
        for club in self.club_checkbox_logo_names_list:
            if name in club.club_name.text_content():
                club.click_on_checkbox()
        return self

    def click_on_club_checkbox_by_index(self, index: int) -> Self:
        self.club_checkbox_logo_names_list[index].click_on_checkbox()
        return self

    @property
    def previous_step_button(self) -> Locator:
        if self._previous_step_button is None:
            self._previous_step_button = self.locator.locator("button.prev-btn")
        return self._previous_step_button

    def click_previous_step_button(self) -> 'AddCenterStepThree':
        self.previous_step_button.click()
        from speak_ukrainian.src.components.add_center_popup.add_center_step_three import AddCenterStepThree
        return AddCenterStepThree(self.locator)

    @property
    def complete_button(self) -> Locator:
        if self._complete_button is None:
            self._complete_button = self.locator.locator("button.finish-btn")
        return self._complete_button

    def click_complete_button(self) -> None:
        self.complete_button.click()
