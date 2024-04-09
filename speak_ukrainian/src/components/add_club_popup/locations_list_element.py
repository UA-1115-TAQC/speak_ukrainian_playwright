from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from speak_ukrainian.src.elements.base_element import BaseElement


class LocationsListElement(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._location_title = None
        self._location_description = None
        self._edit_icon = None
        self._delete_icon = None

    @property
    def location_title(self) -> Locator:
        if self._location_title is None:
            self._location_title = self.locator.locator("h4.ant-list-item-meta-title")
        return self._location_title

    @property
    def location_description(self) -> Locator:
        if self._location_description is None:
            self._location_description = self.locator.locator("div.ant-list-item-meta-description")
        return self._location_description

    @property
    def edit_icon(self) -> Locator:
        if self._edit_icon is None:
            self._edit_icon = self.locator.get_by_label("edit")
        return self._edit_icon

    def click_edit_icon(self) -> AddLocationPopUp:
        self.edit_icon.click()
        filter_locator = self.locator.page.locator("div.add-club-header", hasText="Додати локацію")
        return AddLocationPopUp(self.locator.page.locator("div.add-modal-club").filter(has=filter_locator))

    @property
    def delete_icon(self) -> Locator:
        if self._delete_icon is None:
            self._delete_icon = self.locator.get_by_label("delete")
        return self._delete_icon

    def click_delete_icon(self) -> Locator:
        self.delete_icon.click()
        return self.pop_confirm_container

    @property
    def pop_confirm_container(self) -> Locator:
        hidden_locator_class = self.locator.page.locator("div.ant-popover-hidden")
        return self.locator.page.locator("div.ant-popover-inner-content", has_not=hidden_locator_class)

    @property
    def pop_confirm_icon(self):
        return self.pop_confirm_container.get_by_label("exclamation-circle")

    @property
    def pop_confirm_title(self):
        return self.pop_confirm_container.locator("div.ant-popconfirm-title")

    @property
    def pop_confirm_ok_button(self):
        return self.pop_confirm_container.get_by_role("button", name="Так")

    def click_pop_confirm_ok_button(self) -> Self:
        self.pop_confirm_ok_button.click()
        return self

    @property
    def pop_confirm_cancel_button(self):
        return self.pop_confirm_container.get_by_role("button", name="Ні")

    def click_pop_confirm_cancel_button(self) -> Self:
        self.pop_confirm_cancel_button.click()
        return self
