from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import AddClubPopUp, AddClubSider
from speak_ukrainian.src.components.add_club_popup.add_club_step_one import AddClubStepOne
from speak_ukrainian.src.components.add_club_popup.add_club_step_three import AddClubStepThree
from speak_ukrainian.src.components.add_club_popup.add_club_step_two import AddClubStepTwo
from speak_ukrainian.src.elements.dropdown import Dropdown
from speak_ukrainian.src.elements.input_with_icons_and_errors import InputValidationStaticIconsAndErrors


class EditClubStepOne(AddClubStepOne):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    def click_on_category_by_name(self, value: str) -> Self:
        for category in self.categories_node_list:
            if value in category.text_content():
                category.click()
        return self

    def get_category_texts_list(self) -> list[str]:
        return [category.text_content() for category in self.categories_node_list]

    def get_checked_category_texts_list(self) -> list[str]:
        return [category.text_content() for category in self.checked_categories_list]

    @property
    def category_error(self) -> Locator:
        return self.locator.locator("#edit_category_selectedCategories_help")

    @property
    def center_dropdown_element(self) -> Dropdown:
        return Dropdown(self.locator.locator("div.add-club-select"), "edit_category_centerId_list")


class EditClubStepTwo(AddClubStepTwo):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def work_days_list(self) -> list[Locator]:
        return self.locator.locator("label.ant-checkbox-wrapper").all()

    @property
    def telephone_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_Телефон")))

    @property
    def facebook_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_Facebook")))

    @property
    def whatsapp_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_WhatsApp")))

    @property
    def email_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_Пошта")))

    @property
    def skype_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_Skype")))

    @property
    def site_input_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#basic_Site")))


class EditClubStepThree(AddClubStepThree):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def gallery_title(self) -> Locator:
        if self._gallery_title is None:
            self._gallery_title = self.locator.get_by_text("Оновити галерею", exact=True)
        return self._gallery_title

    @property
    def description_textarea(self) -> Locator:
        return self.locator.locator("#basic_descriptionText")

    @property
    def error_messages_list(self) -> list[Locator]:
        return self.locator.locator("#basic_descriptionText_help").locator("div.ant-form-item-explain-error").all()


class EditClubPopUp(AddClubPopUp):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def step_one_container(self) -> EditClubStepOne:
        return EditClubStepOne(self._step_container)

    @property
    def step_two_container(self) -> EditClubStepTwo:
        return EditClubStepTwo(self._step_container)

    @property
    def step_three_container(self) -> EditClubStepThree:
        return EditClubStepThree(self._step_container)
