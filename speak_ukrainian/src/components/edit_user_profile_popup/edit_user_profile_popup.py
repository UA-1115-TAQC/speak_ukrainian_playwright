from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp


class EditUserProfilePopup(BasePopUp):

    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._edit_user_popup_title = None

    def __int__(self, locator: Locator):
        super().__init__(locator)
        self._edit_user_popup_title = None
        self._user_icon = None
        self._user_type_button = None
        self._manager_icon = None
        self._country_code = None
        self._upload_user_photo_element = None
        self._upload_user_photo_input = None
        self._photo_title = None
        self._question_circle_for_photo = None
        self._photo_tooltip_form = None
        self._checkbox_change_password_title = None
        self._checkbox_change_password_input = None
        self._submit_button = None

    @property
    def popup_title(self) -> Locator:
        if self._edit_user_popup_title is None:
            self._edit_user_popup_title = self.locator.locator("div.edit-header")
        return self._edit_user_popup_title

    @property
    def get_user_icon(self) -> Locator:
        if self._user_icon is None:
            self._user_icon = self.locator.locator("xpath=./descendant::div[@class='ellipse'][1]")
        return self._user_icon

    @property
    def user_type_button(self) -> Locator:
        return self.locator.locator("span.ant-radio-button").and_(self.locator.get_by_role("radio", name="ROLE_USER"))

    def click_on_user_type_button(self):
        return self.user_type_button.click()

    @property
    def get_manager_icon(self) -> Locator:
        if self._manager_icon is None:
            self._manager_icon = self.locator.locator("xpath=./descendant::div[@class='ellipse'][2]")
        return self._manager_icon

    @property
    def manager_type_button(self) -> Locator:
        return self.locator.locator("span.ant-radio-button").and_(self.locator.get_by_role("radio", name="ROLE_MANAGER"))

    def click_on_manager_type_button(self):
        return self.manager_type_button.click()

    @property
    def last_name_element(self):
        return (self.locator.locator("div.user-edit-input")
                .filter(has=self.locator.get_by_role("alert", name="Необхідне поле")))

    @property
    def first_name_element(self):
        return self.locator.locator("div.user-edit-input").filter()

    @property
    def phone_country_code(self) -> Locator:
        if self._country_code is None:
            self._country_code = self.locator.locator("span.ant-input-group-addon")
        return self._country_code

    @property
    def photo_title(self) -> Locator:
        if self._photo_title is None:
            self._photo_title = self.locator.get_by_title("Фото")
        return self._photo_title

    @property
    def question_photo_circle(self) -> Locator:
        if self._question_circle_for_photo is None:
            self._question_circle_for_photo = self.locator.get_by_role("img", name="question-circle")
        return self._question_circle_for_photo

    @property
    def submit_button(self) -> Locator:
        if self._submit_button is None:
            self._submit_button = self.locator.get_by_role("button", name="Зберегти зміни")
        return self._submit_button

    def click_on_submit_button(self) -> None:
        self.submit_button.click()

