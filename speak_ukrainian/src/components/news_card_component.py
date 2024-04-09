from playwright._impl._locator import Locator
from ..base import BaseComponent
from ..pages.news_page import NewsPage


class NewsCardComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._news_image = None
        self._news_date = None
        self._news_title = None

    def click_news_card_link(self) -> NewsPage:
        self.locator.get_by_role("link", name="Детальніше", exact=False).click()
        return NewsPage(self.locator.page)

    @property
    def get_news_image_locator(self) -> Locator:
        if not self._news_image:
            self._news_image = self.locator.locator("#newsImage")
        return self._news_image

    @property
    def get_news_date_locator(self) -> Locator:
        if not self._news_date:
            self._news_date = self.locator.locator("#newsDate")
        return self._news_date

    @property
    def get_news_title_locator(self) -> Locator:
        if not self._news_title:
            self._news_title = self.locator.locator("#newsTitle")
        return self._news_title

