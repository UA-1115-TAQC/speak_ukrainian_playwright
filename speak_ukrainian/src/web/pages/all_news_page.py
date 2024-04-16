from playwright._impl._locator import Locator
from playwright._impl._page import Page
from speak_ukrainian.src.base import BasePageWithAdvancedSearch
from speak_ukrainian.src.components.news_card_component import NewsCardComponent
from speak_ukrainian.src.components.club_card_component import ClubCardComponent


class AllNewsPage(BasePageWithAdvancedSearch):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def get_news_containers(self) -> Locator:
        return self.page.locator("#newsContainer")

    @property
    def get_club_containers(self) -> Locator:
        return self.page.locator(".ant-card-bordered")

    @property
    def get_news_cards_list(self) -> list[NewsCardComponent]:
        return [NewsCardComponent(news) for news in self.get_news_containers.all()]

    @property
    def get_club_cards_list(self) -> list[ClubCardComponent]:
        return [ClubCardComponent(club) for club in self.get_club_containers.all()]

    @property
    def get_pagination_locator(self) -> Locator:
        return self.page.locator(".pagination")
