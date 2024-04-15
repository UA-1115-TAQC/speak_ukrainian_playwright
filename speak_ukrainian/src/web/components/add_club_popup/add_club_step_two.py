from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BaseComponent
from speak_ukrainian.src.web.components.add_club_popup.add_club_step_three import AddClubStepThree
from speak_ukrainian.src.web.components.add_club_popup.day_time_checkbox_element import DayTimeCheckboxElement
from speak_ukrainian.src.web.components.add_club_popup.locations_list_element import LocationsListElement
from speak_ukrainian.src.web.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from speak_ukrainian.src.web.elements import InputValidationStaticIconsAndErrors


class AddClubStepTwo(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._locations_title = None
        self._available_online_title = None
        self._info_hint_icon = None
        self._work_hours_title = None
        self._contacts_title = None
        self._next_step_button = None
        self._previous_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.add-club-header")
        return self._popup_title

    @property
    def locations_title(self) -> Locator:
        if self._locations_title is None:
            self._locations_title = self.locator.get_by_text("Локації", exact=True)
        return self._locations_title

    @property
    def no_data_location_element(self) -> Locator:
        return self.locator.locator("div.ant-empty-normal")

    @property
    def add_location_button(self) -> Locator:
        return self.locator.locator("span.add-club-location", has_text="Додати локацію")

    def click_add_location_button(self) -> AddLocationPopUp:
        self.add_location_button.click()
        filter_locator = self.locator.page.locator("div.add-club-header", has_text="Додати локацію")
        return AddLocationPopUp(self.locator.page.locator("div.modal-add-club").filter(has=filter_locator))

    @property
    def get_list_of_location_elements(self) -> list[LocationsListElement]:
        locations_list = self.locator.locator("li.ant-list-item").all()
        return [LocationsListElement(location) for location in locations_list] if locations_list else []

    def get_locations_name_list(self) -> list[str]:
        return [location.get_location_title_text() for location in self.get_list_of_location_elements()]

    @property
    def available_online_title(self) -> Locator:
        if self._available_online_title is None:
            self._available_online_title = self.locator.get_by_text("Доступний онлайн", exact=True)
        return self._available_online_title

    @property
    def switch_button(self) -> Locator:
        return self.locator.get_by_role("switch", exact=True)

    def click_switch_button(self) -> Self:
        self.switch_button.click()
        return self

    def is_switch_button_checked(self) -> bool:
        return self.switch_button.is_checked()

    @property
    def info_hint_icon(self) -> Locator:
        if self._info_hint_icon is None:
            self._info_hint_icon = self.locator.get_by_label("info-circle", exact=True)
        return self._info_hint_icon

    def click_info_hint_icon(self) -> Self:
        self.info_hint_icon.click()
        return self

    @property
    def info_hint_container(self) -> Locator:
        return self.locator.page.get_by_role("tooltip", exact=True)

    @property
    def work_hours_title(self) -> Locator:
        if self._work_hours_title is None:
            self._work_hours_title = self.locator.get_by_text("Години роботи", exact=True)
        return self._work_hours_title

    @property
    def work_days_list(self) -> list[Locator]:
        return self.locator.locator("div.checkbox-item").all()

    def work_days_texts_list(self) -> list[str]:
        return [day.text_content() for day in self.work_days_list]

    def get_day_time_checkbox_elements_collection(self) -> dict[str, DayTimeCheckboxElement]:
        day_time_checkbox_elements_collection = {}
        for day in self.work_days_list:
            checkbox_value = day.locator("input").input_value()
            day_time_checkbox_elements_collection[checkbox_value] = DayTimeCheckboxElement(day)
        return day_time_checkbox_elements_collection

    def click_on_checkbox_by_day(self, day: str):
        self.get_day_time_checkbox_elements_collection().get(day.upper()).click_on_checkbox()
        return self

    def set_time_checkbox_by_day(self, day: str, time_from: str, time_to: str):
        self.get_day_time_checkbox_elements_collection().get(day.upper()).set_time_from_input(time_from)
        self.get_day_time_checkbox_elements_collection().get(day.upper()).set_time_to_input(time_to)
        return self

    @property
    def checked_work_days_list(self) -> list[Locator]:
        return self.locator.get_by_role("checkbox", checked=True).all()

    def checked_work_days_names_list(self) -> list[str]:
        return [day.input_value() for day in self.checked_work_days_list]

    @property
    def contacts_title(self) -> Locator:
        if self._contacts_title is None:
            self._contacts_title = self.locator.get_by_text("Контакти", exact=True)
        return self._contacts_title

    @property
    def telephone_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactТелефон")))

    @property
    def facebook_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactFacebook")))

    @property
    def whatsapp_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactWhatsApp")))

    @property
    def email_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactПошта")))

    @property
    def skype_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactSkype")))

    @property
    def site_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_contactSite")))

    @property
    def next_step_button(self) -> Locator:
        if self._next_step_button is None:
            self._next_step_button = self.locator.get_by_role("button", name="Наступний крок")
        return self._next_step_button

    def click_next_step_button(self) -> AddClubStepThree:
        self.next_step_button.click()
        return AddClubStepThree(self.locator)

    @property
    def previous_step_button(self) -> Locator:
        if self._previous_step_button is None:
            self._previous_step_button = self.locator.get_by_role("button", name="Назад")
        return self._previous_step_button

    def click_previous_step_button(self) -> 'AddClubStepOne':
        self.previous_step_button.click()
        from speak_ukrainian.src.web.components.add_club_popup.add_club_step_one import AddClubStepOne
        return AddClubStepOne(self.locator)
