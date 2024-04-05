from typing import Self

from playwright._impl._locator import Locator
from playwright.sync_api import expect

from speak_ukrainian.src.components.elements.base_element import BaseElement


class UploadedImageElement(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._paper_clip_icon = None
        self._image_title = None

    @property
    def paper_clip_icon(self) -> Locator:
        if self._paper_clip_icon is None:
            self._paper_clip_icon = self.locator.get_by_label("paper-clip")
        return self._paper_clip_icon

    @property
    def image_title(self) -> Locator:
        if self._image_title is None:
            self._image_title = self.locator.locator("span.ant-upload-list-item-name")
        return self._image_title

    @property
    def actions_container(self) -> Locator:
        return self.locator.locator("span.ant-upload-list-item-actions")

    @property
    def delete_image_icon(self) -> Locator:
        return self.actions_container.get_by_title("Remove file", exact=True)

    def click_delete_button(self) -> Self:
        self.delete_image_icon.click()
        return self

    @property
    def error_tooltip(self) -> Locator:
        self.image_title.click()
        return self.locator.get_by_role("tooltip", exact=True)

    @property
    def upload_done(self) -> Locator:
        self.image_title.click()
        return self.locator.locator("div.ant-upload-list-item-done")

    def wait_image_loaded(self) -> Self:
        self.wait_to_be_visible(self.upload_done)
        return self

    def wait_image_changed(self, prev_img: str) -> Self:
        expect(self.image_title).not_to_have_text(prev_img, ignore_case=True)
        self.wait_image_loaded()
        return self
