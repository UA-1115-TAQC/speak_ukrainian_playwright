from playwright._impl._locator import Locator
from typing import Self

from speak_ukrainian.src.base import BasePopUp


class AddChildPopUp(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._name_input = None
        self._last_name_input = None
        self._age_input = None
        self._male_gender = None
        self._female_gender = None
        self._submit_button = None

    @property
    def name_input_element(self) -> Locator:
        self._name_input = self.locator.get_by_label("Ім'я")
        return self._name_input

    def fill_first_name(self, name: str) -> Self:
        return self.name_input_element.fill(name)

    @property
    def last_name_input_element(self) -> Locator:
        self._last_name_input = self.locator.get_by_label("Прізвище")
        return self._last_name_input

    def fill_last_name(self, last_name: str) -> Self:
        return self.last_name_input_element.fill(last_name)

    @property
    def age_input_element(self) -> Locator:
        self._age_input = self.locator.get_by_label("Вік")
        return self._age_input

    def fill_age(self, age: str) -> Self:
        return self.age_input_element.fill(age)

    @property
    def female_gender_element(self) -> Locator:
        self._female_gender = self.locator.get_by_text("Дівчинка")
        return self._female_gender

    def click_female_gender(self) -> Self:
        self.female_gender_element.click()
        return self

    @property
    def male_gender_element(self) -> Locator:
        self._male_gender = self.locator.get_by_text("Хлопчик")
        return self._male_gender

    def click_male_gender(self) -> Self:
        self.male_gender_element.click()
        return self

    @property
    def submit_button_element(self) -> Locator:
        if self._submit_button is None:
            self._submit_button = self.locator.get_by_role("button", name="Додати", exact=True)
            return self._submit_button

    def click_submit_button(self) -> Self:
        self.submit_button_element.click()
        return self
