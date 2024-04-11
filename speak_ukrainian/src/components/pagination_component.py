from speak_ukrainian.src.base import BaseComponent
from playwright.sync_api import expect


class PaginationComponent(BaseComponent):
    ITEMS_XPATH = "//li[contains(@class, 'ant-pagination-item') or contains(@class, 'ant-pagination-jump-')]"

    def __init__(self, locator):
        super().__init__(locator)
        self._previous = None
        self._next = None

    @property
    def previous(self):
        if not self._previous:
            self._previous = self.locator.get_by_title("Previous Page")
        return self._previous

    @property
    def next(self):
        if not self._next:
            self._next = self.locator.get_by_title("Next Page")
        return self._next

    @property
    def items(self):
        return self.locator.locator(self.ITEMS_XPATH).all()

    def click_previous(self):
        self.previous.click()

    def click_next(self):
        self.next.click()

    def is_next_disabled(self):
        return self.next.get_attribute("aria-disabled") == "true"

    def get_last_page(self):
        while not self.is_next_disabled():
            self.click_next()

    def get_item_by_title(self, num):
        for e in self.items:
            if e.get_attribute("title") == num:
                return e
        return None

    def click_page_by_title(self, num):
        self.get_item_by_title(num).click()

    def scroll_into_view(self):
        self.next.scroll_into_view_if_needed()


class ClubsPaginationComponent(PaginationComponent):
    FIRST_CLUB_NAME_XPATH = "//div[contains(@class,'content-clubs-list')]//div[contains(@class, 'ant-card-body')]//div[@class='title']//div[@class='name']"

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def first_club_name(self):
        return self.locator.page.locator(self.FIRST_CLUB_NAME_XPATH).nth(0)

    def click_next(self):
        first_club_text = self.first_club_name.text_content()
        self.next.click()
        expect(self.first_club_name).not_to_contain_text(first_club_text)
