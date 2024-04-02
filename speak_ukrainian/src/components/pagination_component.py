from speak_ukrainian.src.base import BaseComponent

ITEMS_XPATH = "//li[contains(@class, 'ant-pagination-item') or contains(@class, 'ant-pagination-jump-')]"


class PaginationComponent(BaseComponent):

    def __init__(self, locator):
        super().__init__(locator)
        self._previous = None
        self._next = None
        self._items = None

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
        if not self._items:
            self._items = self.locator.locator(ITEMS_XPATH).all()
        return self._items

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
