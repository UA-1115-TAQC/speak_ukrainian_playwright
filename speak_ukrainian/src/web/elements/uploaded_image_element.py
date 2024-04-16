from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.web.elements import BaseElement


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

