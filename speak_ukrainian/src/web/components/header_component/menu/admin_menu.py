from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BaseComponent, BasePage
from speak_ukrainian.src.web.components.add_center_popup.add_center_popup_component import AddCenterPopUp
from speak_ukrainian.src.web.components.add_club_popup import AddClubPopUp
from speak_ukrainian.src.web.pages.search_certificate.search_certificate import SearchCertificatePage
from speak_ukrainian.src.web.profile_page import ProfilePage


class AdminMenu(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._add_club = None
        self._add_center = None
        self._search_certificate = None
        self._content = None
        self._location = None
        self._clubs = None
        self._page = None
        self._profile = None
        self._logout = None

    @property
    def add_club(self) -> Locator:
        if self._add_club is None:
            self._add_club = self.locator.locator("li[data-menu-id*=add_club]")
        return self._add_club

    @property
    def add_center(self) -> Locator:
        if self._add_center is None:
            self._add_center = self.locator.locator("li[data-menu-id*=add_centre]")
        return self._add_center

    @property
    def search_certificate(self) -> Locator:
        if self._search_certificate is None:
            self._search_certificate = self.locator.locator("li[data-menu-id*=search_certificates]")
        return self._search_certificate

    @property
    def content(self) -> Locator:
        if self._content is None:
            self._content = self.locator.get_by_role("menuitem", name="Контент right")
        return self._content

    @property
    def location(self) -> Locator:
        if self._location is None:
            self._location = self.locator.get_by_role("menuitem", name="Локації right")
        return self._location

    @property
    def clubs(self) -> Locator:
        if self._clubs is None:
            self._clubs = self.locator.get_by_role("menuitem", name="Гуртки right")
        return self._clubs

    @property
    def pages(self) -> Locator:
        if self._page is None:
            self._page = self.locator.get_by_role("menuitem", name="Сторінка right")
        return self._page

    @property
    def profile(self) -> Locator:
        if self._profile is None:
            self._profile = self.locator.locator("li[data-menu-id*=profile]")
        return self._profile

    @property
    def logout(self) -> Locator:
        if self._logout is None:
            self._logout = self.locator.locator("li[data-menu-id*=logout]")
        return self._logout

    @property
    def open_add_club_form(self) -> AddClubPopUp:
        self.add_club.click()
        return AddClubPopUp(self.locator.page.locator("div.modal-add-club"))

    @property
    def open_add_center_form(self) -> AddCenterPopUp:
        self.add_center.click()
        return AddCenterPopUp(self.locator.page.locator("div.addCenter"))

    @property
    def open_search_certificate_page(self) -> SearchCertificatePage:
        self.search_certificate.click()
        return SearchCertificatePage(self.locator.page)

    @property
    def open_profile_page(self) -> ProfilePage:
        self.profile.click()
        return ProfilePage(self.locator.page)

    def click_logout_button(self) -> BasePage:
        self.logout.click()
        return BasePage(self.locator.page)

    def click_location(self) -> None:  # TODO
        self.location.click()

    def click_content(self) -> None:  # TODO
        self.content.click()

    def click_clubs(self) -> None:  # TODO
        self.clubs.click()

    def click_pages(self) -> None:  # TODO
        self.pages.click()
