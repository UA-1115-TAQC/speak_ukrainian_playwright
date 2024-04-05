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
        self._manager_type_button = None
        self._last_name_input_element = None
        self._first_name_input_element = None
        self._phone_input_element = None
        self._phone_country_code = None
        self._email_input_element = None
        self._upload_user_photo_element = None
        self._upload_user_photo_input = None
        self._photo_title = None
        self._question_circle_for_photo = None
        self._photo_tooltip_form = None
        self._checkbox_change_password_title = None
        self._checkbox_change_password_input = None
        self._current_password_input_element = None
        self._new_password_input_element = None
        self._confirm_password_input_element = None
        self._submit_button = None

    @property
    def popup_title(self) -> Locator:
        if self._edit_user_popup_title is None:
            self._edit_user_popup_title = self.locator.locator(".edit-header")
            return self._edit_user_popup_title

    @property
    def get_user_icon(self) -> Locator:
        if self._user_icon is None:
            self._user_icon = self.locator.locator("")
