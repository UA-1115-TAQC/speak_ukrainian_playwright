from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.club_card_component import ClubCardComponent
from speak_ukrainian.src.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from speak_ukrainian.src.components.list_control_component import ListControlComponent
from speak_ukrainian.src.components.pagination_component import PaginationComponent

SEARCH_CLUB_HEADER_XPATH = "//div[contains(@class, 'lower-header-box')]"
PAGINATION_XPATH = "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]"
LIST_CONTROL_XPATH = "//div[contains(@class, 'club-list-control')]"
SEARCH_SIDER_XPATH = "//div[contains(@class, 'sider')]"
CLUB_CARDS_XPATH = "//div[contains(@class,'content-clubs-list')]/child::div"
# CENTER_CARDS_XPATH = "//div[contains(@class,'content-center-list')]/child::div"


class ClubsPage (BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def search_clubs_header(self):
        return AdvancedSearchClubsHeaderComponent(self.page.locator(SEARCH_CLUB_HEADER_XPATH))

    @property
    def pagination(self):
        return PaginationComponent(self.page.locator(PAGINATION_XPATH))

    @property
    def list_control(self):
        return ListControlComponent(self.page.locator(LIST_CONTROL_XPATH))

    @property
    def club_card_list(self):
        card_list = self.page.locator(CLUB_CARDS_XPATH).all()
        return [ClubCardComponent(club) for club in card_list]
