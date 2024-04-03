from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.add_club_popup.add_club_step_two import AddClubStepTwo
from speak_ukrainian.src.elements.dropdown import Dropdown
from speak_ukrainian.src.elements.input_with_icons_and_errors import InputWithValidationIconAndErrors
from speak_ukrainian.src.elements.number_input_element import NumberInput


class AddClubStepOne(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._club_name_title = None
        self._categories_title = None
        self._age_title = None
        self._center_dropdown_title = None
        self._next_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.add-club-header")
        return self._popup_title

    @property
    def club_name_title(self) -> Locator:
        if self._club_name_title is None:
            self._club_name_title = self.locator.get_by_text("Назва", exact=True)
        return self._club_name_title

    @property
    def name_input_element(self) -> InputWithValidationIconAndErrors:
        return InputWithValidationIconAndErrors(self.locator.locator("div.ant-form-item.add-club-row").first)

    @property
    def categories_title(self) -> Locator:
        if self._categories_title is None:
            self._categories_title = self.locator.get_by_text("Категорія", exact=True)
        return self._categories_title

    @property
    def categories_node_list(self) -> list[Locator]:
        return self.locator.locator("label.ant-checkbox-wrapper").all()

    @property
    def categories_checkbox_list(self) -> list[Locator]:
        return self.locator.get_by_role("checkbox", exact=True).all()

    def click_on_category_by_name(self, value: str) -> Self:
        for category in self.categories_checkbox_list:
            if category.input_value() == value:
                category.check()
        return self

    def get_category_texts_list(self) -> list[str]:
        return [category.input_value() for category in self.categories_checkbox_list]

    @property
    def checked_categories_list(self) -> list[Locator]:
        return self.locator.get_by_role("checkbox", checked=True, exact=True).all()

    def get_checked_category_texts_list(self) -> list[str]:
        return [category.input_value() for category in self.checked_categories_list]

    @property
    def category_error(self) -> Locator:
        return self.locator.locator("#basic_categories_help")

    @property
    def age_title(self) -> Locator:
        if self._age_title is None:
            self._age_title = self.locator.get_by_text("Вік дитини", exact=True)
        return self._age_title

    @property
    def min_age_input_element(self) -> NumberInput:
        return NumberInput(self.locator.locator("span.add-club-age div.ant-form-item").first)

    @property
    def max_age_input_element(self) -> NumberInput:
        return NumberInput(self.locator.locator("span.add-club-age div.ant-form-item").last)

    @property
    def center_dropdown_title(self) -> Locator:
        if self._center_dropdown_title is None:
            self._center_dropdown_title = self.locator.get_by_text("Вік дитини", exact=True)
        return self._center_dropdown_title

    @property
    def center_dropdown_element(self) -> Dropdown:
        return Dropdown(self.locator.locator("div.add-club-select"))

    @property
    def next_step_button(self) -> Locator:
        if self._next_step_button is None:
            self._next_step_button = self.locator.get_by_role("button", name="Наступний крок")
        return self._next_step_button

    def click_next_step_button(self) -> AddClubStepTwo:
        self.next_step_button.click()
        return AddClubStepTwo(self.locator)
