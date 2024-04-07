from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent, BasePage
from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import AddClubPopUp


class UserMenu(BaseComponent):

    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._add_club = None
        self._add_center = None
        self._search_certificate = None
        self._search_name = None
        self._profile = None
        self._logout = None

    @property
    def add_club(self) -> Locator:
        if self._add_club is None:
            self._add_club = self.locator.get_by_role("menuitem", name="Додати гурток")
        return self._add_club

    @property
    def add_center(self) -> Locator:
        if self._add_center is None:
            self._add_center = self.locator.get_by_role("menuitem", name="Додати центр")
        return self._add_center

    @property
    def search_certificate(self) -> Locator:
        if self._search_certificate is None:
            self._search_certificate = self.locator.get_by_role("link", name="Пошук сертифікатів")
        return self._search_certificate

    @property
    def profile(self) -> Locator:
        if self._profile is None:
            self._profile = self.locator.get_by_role("link", name="Особистий кабінет")
        return self._profile

    @property
    def logout(self) -> Locator:
        if self._logout is None:
            self._logout = self.locator.get_by_role("menuitem", name="Вийти")
        return self._logout

    @property
    def open_add_club_form(self) -> AddClubPopUp:
        self.add_club.click()
        return AddClubPopUp(self.locator.locator("div.modal-add-club"))

    def open_add_center_form(self):  # TODO
        self.add_center.click()
        # self.locator.locator("div.addCenter")
        pass

    def open_search_certificate_page(self):  # TODO
        self.search_certificate.click()
        # self.locator.page
        pass

    def open_profile_page(self):  # TODO
        self.profile.click()
        # self.locator.page
        pass

    @property
    def click_logout_button(self) -> BasePage:
        self.logout.click()
        return BasePage(self.locator.page)
