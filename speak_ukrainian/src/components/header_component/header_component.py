from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import AddClubPopUp
from speak_ukrainian.src.components.header_component.menu.admin_menu import AdminMenu
from speak_ukrainian.src.components.header_component.menu.guest_menu import GuestMenu
from speak_ukrainian.src.components.header_component.menu.user_menu import UserMenu
from speak_ukrainian.src.pages.all_news_page import AllNewsPage


class HeaderComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._club_container = None
        self._news_container = None
        self._challenge_container = None
        self._about_us_container = None
        self._service_container = None
        self._add_club_button = None
        self._location_icon = None
        self._location_button = None
        self._avatar = None
        self._profile_menu_button = None

    @property
    def get_news_container_locator(self) -> Locator:
        if not self._news_container:
            self._news_container = (self.locator.locator("li", has_text="Новини"))
        return self._news_container

    @property
    def get_club_container(self) -> Locator:
        if not self._club_container:
            self._club_container = (self.locator.locator("li", has_text="Гуртки"))
        return self._club_container

    @property
    def get_challenge_container(self) -> Locator:
        if not self._challenge_container:
            self._challenge_container = (self.locator.locator("li", has_text="Челендж"))
        return self._challenge_container

    @property
    def get_about_us_container(self) -> Locator:
        if not self._about_us_container:
            self._about_us_container = (self.locator.locator("li", has_text="Про нас"))
        return self._about_us_container

    @property
    def get_service_container(self) -> Locator:
        if not self._service_container:
            self._service_container = (self.locator.locator("li", has_text="Послуги"))
        return self._service_container

    @property
    def profile_menu_button(self) -> Locator:
        return self.locator.locator("div.ant-dropdown-trigger.user-profile")

    @property
    def register_menu_button(self) -> Locator:
        return self.locator.locator("li", has_text="Зареєструватися")

    @property
    def login_menu_button(self) -> Locator:
        return self.locator.locator("li", has_text="Увійти")

    @property
    def get_add_club_button(self) -> Locator:
        if not self._add_club_button:
            self._add_club_button = (self.locator.get_by_role("button", name="Додати гурток"))
        return self._add_club_button

    @property
    def get_location_icon(self) -> Locator:
        if not self._location_icon:
            self._location_icon = (self.locator.locator("span[aria-label='environment']"))
        return self._location_icon

    @property
    def get_location_button(self) -> Locator:
        if not self._location_button:
            self._location_button = (self.locator.locator("div.city"))
        return self._location_button

    @property
    def get_avatar(self) -> Locator:
        if not self._avatar:
            self._avatar = (self.locator.locator("span.ant-avatar"))
        return self._avatar

    @property
    def get_profile_menu_button(self) -> Locator:
        if not self._profile_menu_button:
            self._profile_menu_button = (self.locator.locator("div.user-profile"))
        return self._profile_menu_button

    def click_challenge_button(self):
        self.get_challenge_container.click()

    def click_club_button(self):
        self.get_club_container.click()

    def click_news_button(self) -> AllNewsPage:
        self.get_news_container_locator.click()
        self.locator.page.wait_for_selector(selector="#newsContainer", timeout=5000)
        return AllNewsPage(self.locator.page)

    def click_about_us_button(self):
        self.get_about_us_container.click()

    def click_service_button(self):
        self.get_service_container.click()

    def click_add_club_button(self):
        if self.get_add_club_button.is_visible():
            self.get_add_club_button.click()
            return AddClubPopUp(self.locator.page.locator("//div[contains(@class,'modal-add-club')]"))

    #  ClubsPage will be returned
    def select_city(self, city: str):
        self.get_location_button.click()
        self.locator.page.get_by_text(text=city, exact=True).click()

    def get_city_locators_list(self) -> Locator:
        self.get_location_button.click()
        return (self.locator.page.locator("div[class*=placement-bottom]").locator("li"))

    @property
    def open_guest_menu(self) -> GuestMenu:
        self.get_profile_menu_button.click()
        return GuestMenu(self.locator.page.locator("ul.ant-dropdown-menu-light"))

    @property
    def open_user_menu(self) -> UserMenu:
        self.get_profile_menu_button.click()
        return UserMenu(self.locator.page.locator("ul.ant-dropdown-menu-light"))

    @property
    def open_admin_menu(self) -> AdminMenu:
        self.get_profile_menu_button.click()
        return AdminMenu(self.locator.page.locator("ul.ant-dropdown-menu-light"))
