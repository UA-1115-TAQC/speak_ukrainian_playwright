from speak_ukrainian.src.web.base import BasePage
from speak_ukrainian.src.web.components.center_card_component import CenterCardComponent
from speak_ukrainian.src.web.components.club_card_component import ClubCardComponent
from speak_ukrainian.src.web.components.clubs_page_components.list_control_component import ListControlComponent
from speak_ukrainian.src.web.components.clubs_page_components.search_sider_component import SearchSiderComponent

from speak_ukrainian.src.web.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent

from speak_ukrainian.src.web.components.pagination_component import ClubsPaginationComponent


class ClubsPage (BasePage):
    SEARCH_CLUB_HEADER_XPATH = "//div[contains(@class, 'lower-header-box')]"
    PAGINATION_XPATH = "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]"
    LIST_CONTROL_XPATH = "//div[contains(@class, 'club-list-control')]"
    SEARCH_SIDER_XPATH = "//div[contains(@class, 'ant-layout-sider-children')]"
    CLUB_CARDS_XPATH = "//div[contains(@class,'content-clubs-list')]/div"
    CENTER_CARDS_XPATH = "//div[contains(@class,'content-center-list')]/div"

    def __init__(self, page):
        super().__init__(page)
        self._search_clubs_header = None

    @property
    def search_clubs_header(self):
        if not self._search_clubs_header:
            self._search_clubs_header = AdvancedSearchClubsHeaderComponent(self.page.locator(self.SEARCH_CLUB_HEADER_XPATH))
        return self._search_clubs_header

    @property
    def pagination(self) -> ClubsPaginationComponent:
        if self.is_element_present(self.PAGINATION_XPATH):
            return ClubsPaginationComponent(self.page.locator(self.PAGINATION_XPATH))

    @property
    def list_control(self):
        if self.is_element_present(self.LIST_CONTROL_XPATH):
            return ListControlComponent(self.page.locator(self.LIST_CONTROL_XPATH))

    @property
    def search_sider(self):
        if self.is_element_present(self.SEARCH_SIDER_XPATH):
            return SearchSiderComponent(self.page.locator(self.SEARCH_SIDER_XPATH))

    @property
    def card_list(self):
        if self.is_element_present(self.SEARCH_SIDER_XPATH) and self.search_sider.checked_radio_button.get_attribute("innerText") == "Центр":
            return self.get_center_card_list()
        else:
            return self.get_club_card_list()

    def get_club_card_list(self):
        card_list = self.page.locator(self.CLUB_CARDS_XPATH).all()
        return [ClubCardComponent(center) for center in card_list]

    def get_center_card_list(self):
        card_list = self.page.locator(self.CENTER_CARDS_XPATH).all()
        return [CenterCardComponent(club) for club in card_list]

    def is_element_present(self, xpath_name):
        return self.page.locator(xpath_name).is_visible()

    def is_card_list_empty(self):
        return len(self.card_list) == 0
