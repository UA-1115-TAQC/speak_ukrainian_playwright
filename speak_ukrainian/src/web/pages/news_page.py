from playwright._impl._locator import Locator
from playwright._impl._page import Page
from ..base import BasePage, BaseCarousel


class NewsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._news_title = None
        self._news_image = None
        self._news_date = None
        self._news_content = None
        self._help_project_button = None
        self._news_carousel_title = None
        self._news_carousel_block = None

    @property
    def get_news_title(self) -> Locator:
        if not self._news_title:
            self._news_title = (self.page
                                .locator("#major-title"))
        return self._news_title

    @property
    def get_news_image(self) -> Locator:
        if not self._news_image:
            self._news_image = (self.page
                                .locator(".image"))
        return self._news_image

    @property
    def get_news_date(self) -> Locator:
        if not self._news_date:
            self._news_date = (self.page
                               .locator("#date"))
        return self._news_date

    @property
    def get_news_content(self) -> Locator:
        if not self._news_content:
            self._news_content = (self.page
                                  .locator(".content-text"))
        return self._news_content

    @property
    def get_help_project_button(self) -> Locator:
        if not self._help_project_button:
            self._help_project_button = (self.page
                                         .get_by_role("button", name="Допомогти проєкту"))
        return self._help_project_button

    @property
    def get_news_carousel_title(self) -> Locator:
        if not self._news_carousel_title:
            self._news_carousel_title = (self.page
                                         .locator(".title"))
        return self._news_carousel_title

    @property
    def get_news_carousel_block(self):
        if not self._news_carousel_block:
            self._news_carousel_block = BaseCarousel((self.page
                                                      .locator(".news-carousel-block")))
        return self._news_carousel_block

    def click_carousel_right_arrow_button(self):
        self.get_news_carousel_block.get_right_arrow_button.last.click()
        return self

    def click_carousel_left_arrow_button(self):
        self.get_news_carousel_block.get_left_arrow_button.click()
        return self

    @property
    def get_list_news_card(self) -> list['NewsCardComponent']:
        from ..components.news_card_component import NewsCardComponent
        self.page.wait_for_selector(selector=".slick-active")
        news_locator = (self.get_news_carousel_block
                        .get_carousel_container
                        .locator("div.slick-active").all())
        return [NewsCardComponent(news) for news in news_locator]

    def click_carousel_slick_dot(self, index: int):
        self.get_news_carousel_block.click_slick_dot_by_index(index)
        return self

