from playwright._impl._locator import Locator
from ..base import BaseComponent


class NewsCardComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    #  NewsPage will be returned
    def click_news_card_link(self):
        self.locator.get_by_role("link", name="Детальніше ", exact=False).click()

    @property
    def get_news_image_locator(self) -> Locator:
        return self.locator.locator("#newsImage")

    @property
    def get_news_date_locator(self) -> Locator:
        return self.locator.locator("#newsDate")

    @property
    def get_news_title_locator(self) -> Locator:
        return self.locator.locator("#newsTitle")

