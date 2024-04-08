from typing import Self

from playwright._impl._locator import Locator
from playwright._impl._page import Page

from speak_ukrainian.src.base import BasePage, BaseComponent


class CertificateTable(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def table_header_list(self) -> list[Locator]:
        return self.locator.locator("thead.ant-table-thead th").all()

    @property
    def member_header(self) -> Locator:
        return next((head_title for head_title in self.table_header_list if "Учасник" in head_title.text_content()),
                    None)

    @property
    def email_header(self) -> Locator:
        return next(
            (head_title for head_title in self.table_header_list if "Електронна пошта" in head_title.text_content()),
            None)

    @property
    def serial_number_header(self) -> Locator:
        return next(
            (head_title for head_title in self.table_header_list if "Електронна пошта" in head_title.text_content()),
            None)

    @property
    def date_of_issue_header(self) -> Locator:
        return next((head_title for head_title in self.table_header_list if "Дата видачі" in head_title.text_content()),
                    None)

    @property
    def time_duration_header(self) -> Locator:
        return next(
            (head_title for head_title in self.table_header_list if "Тривалість челенджу" in head_title.text_content()),
            None)

    @property
    def certificate_status_header(self) -> Locator:
        return next(
            (head_title for head_title in self.table_header_list if "Статус видачі" in head_title.text_content()), None)


class SearchCertificatePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._search_certificate_title = None
        self._result_searching_title = None
        self._search_icon = None
        self._search_button = None
        self._clear_searching_text_button = None
        self._search_input = None
        self._certificate_table = None

    @property
    def search_certificate_title(self):
        if self._search_certificate_title is None:
            self._search_certificate_title = self.page.get_by_role("heading", name="Пошук сертифікатів")
        return self._search_certificate_title

    @property
    def search_result_searching_title(self):
        if self._result_searching_title is None:
            self._result_searching_title = self.page.get_by_role("heading", name="Немає даних для відображення")
        return self._result_searching_title

    @property
    def search_icon(self):
        if self._search_icon is None:
            self._search_icon = self.page.locator("span[aria-label=search]")
        return self._search_icon

    @property
    def search_button(self):
        if self._search_button is None:
            self._search_button = self.page.get_by_role("button", name="search")
        return self._search_button

    @property
    def clear_searching_text_button(self):
        if self._clear_searching_text_button is None:
            self._clear_searching_text_button = self.page.get_by_role("button", name="close-circle")
        return self._clear_searching_text_button

    @property
    def search_input(self):
        if self._search_input is None:
            self._search_input = self.page.locator("div.searchCertificateUser input")
        return self._search_input

    @property
    def certificate_table(self) -> Locator:
        if self._certificate_table is None:
            self._certificate_table = self.page.locator("div.certificateTable")
        return self._certificate_table

    def click_search_button(self) -> CertificateTable:
        self.search_button.click()
        return CertificateTable(self.certificate_table)

    def click_clear_search_button(self) -> Self:
        self.clear_searching_text_button.click()
        return self

    def set_search_input_value(self, value: str) -> Self:
        self.search_input.fill(value)
        return self

    def get_search_input_value(self) -> Self:
        return self.search_input.get_attribute("value")
