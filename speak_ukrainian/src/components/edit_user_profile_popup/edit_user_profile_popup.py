from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp
from speak_ukrainian.src.elements.input_with_icons_and_errors import InputWithLabelValidationIconAndErrors


class EditUserProfilePopup(BasePopUp):

    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._edit_user_popup_title = None

    def __int__(self, locator: Locator):
        super().__init__(locator)
        self._edit_user_popup_title = None
        self._country_code = None
        self._photo_title = None
        self._question_circle_for_photo = None
        self._checkbox_title = None
        self._submit = None

    @property
    def popup_title(self) -> Locator:
        if self._edit_user_popup_title is None:
            self._edit_user_popup_title = self.locator.locator("div.edit-header")
        return self._edit_user_popup_title

    @property
    def user_type_button(self) -> Locator:
        return self.locator.locator("span").filter(has_text="Відвідувач")

    def click_on_user_type_button(self):
        return self.user_type_button.click()

    @property
    def manager_type_button(self) -> Locator:
        return self.locator.locator("span").filter(has_text="Керівник")

    def click_on_manager_type_button(self):
        return self.manager_type_button.click()

    @property
    def last_name_element(self) -> InputWithLabelValidationIconAndErrors:
        return InputWithLabelValidationIconAndErrors(
            self.locator.locator("xpath=./descendant::div[contains(@class,'user-edit-input')][1]"))

    @property
    def first_name_element(self) -> InputWithLabelValidationIconAndErrors:
        return InputWithLabelValidationIconAndErrors(
            self.locator.locator("xpath=./descendant::div[contains(@class,'user-edit-input')][2]"))

    @property
    def phone_country_code(self) -> Locator:
        if self._country_code is None:
            self._country_code = self.locator.locator("span.ant-input-group-addon")
        return self._country_code

    @property
    def phone_element(self) -> InputWithLabelValidationIconAndErrors:
        return InputWithLabelValidationIconAndErrors(
            self.locator.locator("xpath=./descendant::div[contains(@class,'user-edit-input')][3]"))

    @property
    def email_element(self):
        return self.locator.get_by_label("Email")

    @property
    def photo_title(self) -> Locator:
        if self._photo_title is None:
            self._photo_title = self.locator.get_by_text("Фото")
        return self._photo_title

    @property
    def question_photo_circle(self) -> Locator:
        if self._question_circle_for_photo is None:
            self._question_circle_for_photo = self.locator.get_by_label("question-circle").locator("svg")
        return self._question_circle_for_photo

    def tooltip_form(self) -> Locator:
        return self.locator.get_by_role("tooltip", name="Приймас зображення формату")

    @property
    def uploaded_photo_element(self):
        return self.locator.locator("xpath=.//span[contains(@class, 'ant-upload-wrapper')]")

    def upload_photo(self, img_path: str) -> Self:
        self.locator.get_by_role("button", name="upload Завантажити фото")
        return self

    @property
    def checkbox_title(self) -> Locator:
        if self._checkbox_title is None:
            self._checkbox_title = self.locator.get_by_text("Змінити пароль")
        return self._checkbox_title

    def click_change_password_checkbox(self):
        return self.locator.get_by_role("checkbox").check()

    @property
    def current_password_input_element(self):
        return (self.locator.locator("xpath=(//div[contains(@class,'item-control-input')]"
                                     "/span[contains(@class,'ant-input-password') "
                                     "and not (contains(@class,'login-box'))])[1]"))

    @property
    def new_password_input_element(self):
        return (self.locator.locator("xpath=(//div[contains(@class,'item-control-input')]"
                                     "/span[contains(@class,'ant-input-password') "
                                     "and not (contains(@class,'login-box'))])[2]"))

    @property
    def get_confirm_password_input_element(self):
        return (self.locator.locator("xpath=(//div[contains(@class,'item-control-input')]"
                                     "/span[contains(@class,'ant-input-password') "
                                     "and not (contains(@class,'login-box'))])[3]"))

    @property
    def submit_button(self) -> Locator:
        return self.locator.get_by_role("button", name="Зберегти зміни")

    def click_on_submit_button(self) -> Self:
        return self.submit_button.click()

