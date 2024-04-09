from typing import Self

from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.elements.galery_image_element import GalleryImageElement
from speak_ukrainian.src.elements.uploaded_image_element import UploadedImageElement


class AddClubStepThree(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._logo_title = None
        self._cover_title = None
        self._gallery_title = None
        self._description_title = None
        self._complete_button = None
        self._previous_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.add-club-header")
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
    def cover_title(self) -> Locator:
        if self._cover_title is None:
            self._cover_title = self.locator.get_by_text("Обкладинка", exact=True)
        return self._cover_title

    @property
    def cover_download_input(self) -> Locator:
        return self.locator.page.locator("#basic_urlBackground")

    @property
    def cover_download_button(self) -> Locator:
        return self.locator.get_by_role("button").filter(has=self.cover_download_input)

    def click_cover_download_button(self) -> Self:
        self.cover_download_button.click()
        return self

    @property
    def cover_uploaded_container(self) -> Locator:
        return (self.locator.locator("div.ant-form-item-control-input-content")
                            .filter(has=self.cover_download_input)
                            .locator("div.ant-upload-list-item-container"))

    @property
    def cover_uploaded_img_element(self) -> UploadedImageElement:
        expect(self.cover_uploaded_container).to_be_visible()
        return UploadedImageElement(self.cover_uploaded_container)

    def upload_cover(self, img_path: str) -> Self:
        if self.cover_uploaded_container.is_visible():
            self.cover_uploaded_img_element.click_delete_button()
            expect(self.cover_uploaded_container).not_to_be_visible()
        self.cover_download_input.set_input_files(img_path)
        expect(self.cover_uploaded_img_element.image_title).to_be_visible()
        return self

    @property
    def gallery_title(self) -> Locator:
        if self._gallery_title is None:
            self._gallery_title = self.locator.get_by_text("Галерея", exact=True)
        return self._gallery_title

    @property
    def gallery_download_input(self) -> Locator:
        return (self.locator.page.locator("div.ant-upload-select")
                            .filter(has=self.locator.page.get_by_label("plus"))
                            .locator("input"))

    @property
    def list_of_gallery_locators(self) -> list[Locator]:
        return (self.locator.locator("div.ant-form-item-control-input-content")
                            .filter(has=self.gallery_download_input)
                            .locator("div.ant-upload-list-item-container")
                            .all())

    @property
    def list_of_gallery_image_elements(self) -> list[GalleryImageElement]:
        return [GalleryImageElement(image) for image in self.list_of_gallery_locators]

    @property
    def gallery_download_button(self) -> Locator:
        return self.locator.get_by_role("button").filter(has=self.gallery_download_input)

    def click_gallery_download_button(self) -> Self:
        self.gallery_download_button.click()
        return self

    @property
    def gallery_uploaded_container(self) -> Locator:
        return (self.locator.locator("div.ant-form-item-control-input-content")
                            .filter(has=self.gallery_download_input)
                            .locator("div.ant-upload-list-item-container"))

    def upload_img_to_gallery(self, img_path: str) -> Self:
        img_count = len(self.list_of_gallery_locators)
        self.gallery_download_input.set_input_files(img_path)
        expect(self.list_of_gallery_image_elements[img_count].preview_image_file).to_be_visible()
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

    def click_previous_step_button(self) -> 'AddClubStepTwo':
        self.previous_step_button.click()
        from speak_ukrainian.src.components.add_club_popup.add_club_step_two import AddClubStepTwo
        return AddClubStepTwo(self.locator)

    @property
    def complete_button(self):
        if self._complete_button is None:
            self._complete_button = self.locator.get_by_role("button", name="Завершити")
        return self._complete_button

    def click_complete_button(self) -> None:
        self.complete_button.click()
