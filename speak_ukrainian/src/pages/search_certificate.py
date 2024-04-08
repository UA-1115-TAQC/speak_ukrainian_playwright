from typing import Self

from playwright._impl._page import Page

from speak_ukrainian.src.base import BasePage


class SearchCertificatePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._search_certificate_title = None
        self._result_searching_title = None
        self._search_icon = None
        self._search_button = None
        self._clear_searching_text_button = None
        self._search_input = None

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

    def click_search_button(self) -> Self:
        self.search_button.click()
        return self

    def click_clear_search_button(self) -> Self:
        self.clear_searching_text_button.click()
        return self

    def set_search_input_value(self, value: str) -> Self:
        self.search_input.fill(value)
        return self

    def get_search_input_value(self) -> Self:
        return self.search_input.get_attribute("value")
