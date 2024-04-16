from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BaseComponent


class ClubCheckboxLogoNameElement(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._club_logo = None
        self._club_name = None

    @property
    def club_checkbox(self) -> Locator:
        return self.locator.locator("input")

    @property
    def club_logo(self) -> Locator:
        if self._club_logo is None:
            self._club_logo = self.locator.locator("img")
        return self._club_logo

    @property
    def club_name(self) -> Locator:
        if self._club_name is None:
            self._club_name = self.locator.locator("span.club-name")
        return self._club_name

    def scroll_to_club(self) -> Self:
        self.locator.scroll_into_view_if_needed()
        return self

    def get_logo_image_path(self) -> str:
        return self.club_logo.get_attribute("src")

    def click_on_checkbox(self) -> Self:
        self.scroll_to_club().club_checkbox.click()
        return self
