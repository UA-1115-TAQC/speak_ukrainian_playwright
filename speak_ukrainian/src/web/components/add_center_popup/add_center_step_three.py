from typing import Self

from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.web.base import BaseComponent
from speak_ukrainian.src.web.components.add_center_popup.add_center_step_four import AddCenterStepFour
from speak_ukrainian.src.web.elements.uploaded_image_element import UploadedImageElement


class AddCenterStepThree(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._logo_title = None
        self._photo_title = None
        self._description_title = None
        self._previous_step_button = None
        self._next_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.modal-title")
        return self._popup_title

    @property
    def logo_title(self) -> Locator:
        if self._logo_title is None:
            self._logo_title = self.locator.get_by_text("Логотип", exact=True)
        return self._logo_title

    @property
    def logo_download_input(self) -> Locator:
        return self.locator.page.locator("#basic_urlLogo")

    @property
    def logo_download_button(self) -> Locator:
        return self.locator.get_by_role("button").filter(has=self.logo_download_input)

    def click_logo_download_button(self) -> Self:
        self.logo_download_button.click()
        return self

    @property
    def logo_uploaded_container(self) -> Locator:
        return (self.locator.locator("div.ant-form-item-control-input-content")
                            .filter(has=self.logo_download_input)
                            .locator("div.ant-upload-list-item-container"))

    @property
    def logo_uploaded_img_element(self) -> UploadedImageElement:
        expect(self.logo_uploaded_container).to_be_visible()
        return UploadedImageElement(self.logo_uploaded_container)

    def upload_logo(self, img_path: str) -> Self:
        if self.logo_uploaded_container.is_visible():
            self.logo_uploaded_img_element.click_delete_button()
            expect(self.logo_uploaded_container).not_to_be_visible()
        self.logo_download_input.set_input_files(img_path)
        expect(self.logo_uploaded_img_element.image_title).to_be_visible()
        return self

    @property
    def photo_title(self) -> Locator:
        if self._photo_title is None:
            self._photo_title = self.locator.get_by_text("Фото", exact=True)
        return self._photo_title

    @property
    def photo_download_input(self) -> Locator:
        return self.locator.page.locator("#basic_urlBackground")

    @property
    def photo_download_button(self) -> Locator:
        return self.locator.get_by_role("button").filter(has=self.photo_download_input)

    def click_photo_download_button(self) -> Self:
        self.photo_download_button.click()
        return self

    @property
    def photo_uploaded_container(self) -> Locator:
        return (self.locator.locator("div.ant-form-item-control-input-content")
                            .filter(has=self.photo_download_input)
                            .locator("div.ant-upload-list-item-container"))

    @property
    def photo_uploaded_img_element(self) -> UploadedImageElement:
        expect(self.photo_uploaded_container).to_be_visible()
        return UploadedImageElement(self.photo_uploaded_container)

    def upload_photo(self, img_path: str) -> Self:
        if self.photo_uploaded_container.is_visible():
            self.photo_uploaded_img_element.click_delete_button()
            expect(self.photo_uploaded_container).not_to_be_visible()
        self.photo_download_input.set_input_files(img_path)
        expect(self.photo_uploaded_img_element.image_title).to_be_visible()
        return self

    @property
    def description_title(self) -> Locator:
        if self._description_title is None:
            self._description_title = self.locator.get_by_text("Опис", exact=True)
        return self._description_title

    @property
    def description_textarea(self) -> Locator:
        return self.locator.locator("#basic_description")

    def get_description_textarea_value(self) -> str:
        return self.wait_to_be_visible(self.description_textarea).input_value()

    def set_description_textarea_value(self, value: str):
        self.wait_to_be_visible(self.description_textarea).fill(value)

    @property
    def textarea_validation_circle_icon(self):
        check_circle = self.locator.get_by_label("check-circle")
        close_circle = self.locator.get_by_label("close-circle")
        expect(check_circle.or_(close_circle)).to_be_visible()
        return check_circle if check_circle.is_visible() else close_circle

    @property
    def error_messages_list(self) -> list[Locator]:
        return self.locator.locator("#basic_description_help").locator("div.ant-form-item-explain-error").all()

    def get_error_messages_text_list(self) -> list[str]:
        return [error.text_content() for error in self.error_messages_list]

    def clear_textarea(self) -> Self:
        self.wait_to_be_visible(self.description_textarea).clear()
        return self

    @property
    def previous_step_button(self):
        if self._previous_step_button is None:
            self._previous_step_button = self.locator.get_by_role("button", name="Назад")
        return self._previous_step_button

    def click_previous_step_button(self) -> 'AddCenterStepTwo':
        self.previous_step_button.click()
        from speak_ukrainian.src.web.components.add_center_popup.add_center_step_two import AddCenterStepTwo
        return AddCenterStepTwo(self.locator)

    @property
    def next_step_button(self):
        if self._next_step_button is None:
            self._next_step_button = self.locator.get_by_role("button", name="Наступний крок")
        return self._next_step_button

    def click_next_step_button(self) -> AddCenterStepFour:
        self.next_step_button.click()
        return AddCenterStepFour(self.locator)
