from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.center_card_component import CenterCardComponent
from speak_ukrainian.src.components.club_card_component import ClubCardComponent
from speak_ukrainian.src.components.clubs_page_components.search_sider_component import SearchSiderComponent
from speak_ukrainian.src.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from speak_ukrainian.src.components.clubs_page_components.list_control_component import ListControlComponent
from speak_ukrainian.src.components.pagination_component import PaginationComponent


class ClubsPage (BasePage):
    SEARCH_CLUB_HEADER_XPATH = "//div[contains(@class, 'lower-header-box')]"
    PAGINATION_XPATH = "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]"
    LIST_CONTROL_XPATH = "//div[contains(@class, 'club-list-control')]"
    SEARCH_SIDER_XPATH = "//div[contains(@class, 'sider')]"
    CLUB_CARDS_XPATH = "//div[contains(@class,'content-clubs-list')]/child::div"
    CENTER_CARDS_XPATH = "//div[contains(@class,'content-center-list')]/child::div"

    def __init__(self, page):
        super().__init__(page)
        self._search_clubs_header = None

    @property
    def search_clubs_header(self):
        if not self._search_clubs_header:
            self._search_clubs_header = AdvancedSearchClubsHeaderComponent(self.page.locator(self.SEARCH_CLUB_HEADER_XPATH))
        return self._search_clubs_header

    @property
    def pagination(self):
        if self.is_element_present(self.PAGINATION_XPATH):
            return PaginationComponent(self.page.locator(self.PAGINATION_XPATH))
        return None

    @property
    def list_control(self):
        if self.is_element_present(self.LIST_CONTROL_XPATH):
            return ListControlComponent(self.page.locator(self.LIST_CONTROL_XPATH))
        return None

    @property
    def search_sider(self):
        if self.is_element_present(self.SEARCH_SIDER_XPATH):
            return SearchSiderComponent(self.page.locator(self.SEARCH_SIDER_XPATH))
        return None

    @property
    def card_list(self):
        if self.is_element_present(self.SEARCH_SIDER_XPATH) and self.search_sider.checked_radio_button.get_attribute("innerText") == "Центр":
            return self.get_center_card_list()
        else:
            return self.get_club_card_list()

    def get_center_card_list(self):
        card_list = self.page.locator(self.CLUB_CARDS_XPATH).all()
        return [ClubCardComponent(club) for club in card_list]

    def get_club_card_list(self):
        center_list = self.page.locator(self.CENTER_CARDS_XPATH).all()
        return [CenterCardComponent(center) for center in center_list]

    def is_element_present(self, xpath_name):
        return self.page.locator(xpath_name)

    def is_card_list_empty(self):
        return len(self.card_list) == 0


# TODO test is_element_present here and seaarch_sider