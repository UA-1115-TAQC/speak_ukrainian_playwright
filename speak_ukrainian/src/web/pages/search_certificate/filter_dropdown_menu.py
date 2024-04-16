from typing import Self

from playwright.sync_api import Locator

from speak_ukrainian.src.web.base import BaseComponent


class FilterDropDownMenu(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def certificate_status_checkbox_list(self) -> list[Locator]:
        return self.locator.locator("li.ant-dropdown-menu-item").all()

    def click_certificate_status(self, status: str) -> Self:
        for checkbox in self.certificate_status_checkbox_list:
            if checkbox.text_content() == status:
                checkbox.click()
                break
        return self

    def certificate_status_text_list(self) -> list[str]:
        return [status.text_content() for status in self.certificate_status_checkbox_list]

    @property
    def selected_certificate_status_list(self) -> list[Locator]:
        return self.locator.locator("li.ant-dropdown-menu-item-selected").all()

    def selected_certificate_status_text_list(self) -> list[str]:
        return [status.text_content() for status in self.selected_certificate_status_list]

    @property
    def reset_button(self) -> Locator:
        return self.locator.get_by_role("button", name="Reset")

    @property
    def submit_button(self) -> Locator:
        return self.locator.get_by_role("button", name="OK")

    def click_reset_button(self) -> Self:
        self.reset_button.click()
        return self

    def click_submit_button(self) -> 'CertificateTable':
        self.submit_button.click()
        from speak_ukrainian.src.web.pages.search_certificate.search_certificate import CertificateTable
        return CertificateTable(self.locator.page.locator("div.certificateTable"))
