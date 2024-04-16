from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.web.elements.uploaded_image_element import UploadedImageElement


class GalleryImageElement(UploadedImageElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def preview_image_file(self) -> Locator:
        return self.actions_container.get_by_title("Preview file", exact=True)

    @property
    def preview_image_icon(self) -> Locator:
        return self.actions_container.get_by_label("eye")

    def click_image_preview_icon(self) -> Self:
        self.actions_container.hover()
        self.preview_image_icon.click()
        return self

    @property
    def preview_close_button(self) -> Locator:
        return self.locator.locator("button.ant-modal-close").last

    def click_preview_close_button(self) -> Self:
        self.preview_close_button.click()
        return self

    def click_image_delete_icon(self) -> Self:
        self.actions_container.hover()
        self.delete_image_icon.click()
        return self

    def click_image_container(self) -> Self:
        self.locator.click()
        return self
