from playwright.sync_api import sync_playwright
from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.club_card_component import ClubCardComponent
from speak_ukrainian.src.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from speak_ukrainian.src.components.list_control_component import ListControlComponent
from speak_ukrainian.src.components.pagination_component import PaginationComponent

SEARCH_CLUB_HEADER_XPATH = "//div[contains(@class, 'lower-header-box')]"
PAGINATION_XPATH = "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]"
LIST_CONTROL_XPATH = "//div[contains(@class, 'club-list-control')]"
CLUB_CARDS_XPATH = "//div[contains(@class,'content-clubs-list')]/child::div"


class ClubsPage (BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._search_clubs_header = None
        self._pagination = None
        self._list_control = None
        self._club_card_list = None

    @property
    def search_clubs_header(self):
        if not self._search_clubs_header:
            self._search_clubs_header = AdvancedSearchClubsHeaderComponent(self.page.locator(SEARCH_CLUB_HEADER_XPATH))
        return self._search_clubs_header

    @property
    def pagination(self):
        if not self._pagination:
            self._pagination = PaginationComponent(self.page.locator(PAGINATION_XPATH))
        return self._pagination

    @property
    def list_control(self):
        if not self._list_control:
            self._list_control = ListControlComponent(self.page.locator(LIST_CONTROL_XPATH))
        return self._list_control

    @property
    def club_card_list(self):
        if not self._club_card_list:
            card_list = self.page.locator(CLUB_CARDS_XPATH).all()
            self._club_card_list = [ClubCardComponent(club) for club in card_list]
        return self._club_card_list


def strt():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/clubs")

        c = ClubsPage(page)
        for club in c.club_card_list:
            print(club.name.text_content())

strt()
