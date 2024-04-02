from speak_ukrainian.src.base import BaseComponent


class ClubCardComponent(BaseComponent):

    def __init__(self, locator):
        super().__init__(locator)
        self._logo = None
        self._name = None

        self._directions = None
        self._description = None
        self._rating = None
        self._address = None
        self._address_location_name = None
        self._online = None
        self._details_button = None

        # self._popup = None
        # self._club_info_popup_root = None

        name = ".//div[contains(@class,'name')]"

    @property
    def name(self):
        if not self._name:
            self._name = self.locator.get_by_title("Next Page")
        return self._name