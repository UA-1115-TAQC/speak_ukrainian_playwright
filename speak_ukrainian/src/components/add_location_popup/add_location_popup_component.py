from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp
from speak_ukrainian.src.elements.dropdown import DropdownWithIconError, Dropdown
from speak_ukrainian.src.elements.input_with_icons_and_errors import InputWithInfoValidationIconsAndErrors, \
    InputWithValidationIconAndErrors


class AddLocationPopUp(BasePopUp):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._name_title = None
        self._city_title = None
        self._district_title = None
        self._station_title = None
        self._address_title = None
        self._coordinates_title = None
        self._telephone_title = None
        self._add_location_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.add-club-header")
        return self._popup_title

    @property
    def name_title(self) -> Locator:
        if self._name_title is None:
            self._name_title = self.locator.get_by_text("Назва", exact=True)
        return self._name_title

    @property
    def name_input_element(self) -> InputWithInfoValidationIconsAndErrors:
        return InputWithInfoValidationIconsAndErrors(self.locator.locator("div.add-club-row")
                                                                 .filter(has=self.locator.page.locator("#name")))

    @property
    def city_title(self) -> Locator:
        if self._city_title is None:
            self._city_title = self.locator.get_by_text("Місто", exact=True)
        return self._city_title

    @property
    def city_dropdown_element(self) -> DropdownWithIconError:
        return DropdownWithIconError(self.locator.locator("div.add-club-row")
                                                 .filter(has=self.locator.page.locator("#cityName")),
                                     "cityName_list")

    @property
    def district_title(self) -> Locator:
        if self._district_title is None:
            self._district_title = self.locator.get_by_text("Район міста", exact=True)
        return self._district_title

    @property
    def district_dropdown_element(self) -> Dropdown:
        return Dropdown(self.locator.locator("div.add-club-row").filter(has=self.locator.page.locator("#districtName")),
                        "districtName_list")

    @property
    def station_title(self) -> Locator:
        if self._station_title is None:
            self._station_title = self.locator.get_by_text("Метро/Місцевість", exact=True)
        return self._station_title

    @property
    def metro_dropdown_element(self) -> Dropdown:
        return Dropdown(self.locator.locator("div.add-club-row").filter(has=self.locator.page.locator("#stationName")),
            "stationName_list")

    @property
    def address_title(self) -> Locator:
        if self._address_title is None:
            self._address_title = self.locator.get_by_text("Адреса", exact=True)
        return self._address_title

    @property
    def address_input_element(self) -> InputWithValidationIconAndErrors:
        return InputWithValidationIconAndErrors(self.locator.locator("div.add-club-row")
                                                            .filter(has=self.locator.page.locator("#address")))

    @property
    def coordinates_title(self) -> Locator:
        if self._coordinates_title is None:
            self._coordinates_title = self.locator.get_by_text("Географічні координати", exact=True)
        return self._coordinates_title

    @property
    def coordinates_input_element(self) -> InputWithValidationIconAndErrors:
        return InputWithValidationIconAndErrors(self.locator.locator("div.add-club-row")
                                                            .filter(has=self.locator.page.locator("#coordinates")))

    @property
    def telephone_title(self) -> Locator:
        if self._telephone_title is None:
            self._telephone_title = self.locator.get_by_text("Номер телефону", exact=True)
        return self._telephone_title

    @property
    def telephone_input_element(self) -> InputWithInfoValidationIconsAndErrors:
        return InputWithInfoValidationIconsAndErrors(self.locator.locator("div.add-club-row")
                                                                 .filter(has=self.locator.page.locator("#phone")))

    @property
    def add_location_button(self) -> Locator:
        return self.locator.get_by_role("button", name="Додати")

    def click_add_location_button(self) -> None:
        self.add_location_button.click()
