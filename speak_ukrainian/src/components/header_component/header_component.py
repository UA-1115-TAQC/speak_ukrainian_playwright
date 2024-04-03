from playwright._impl._locator import Locator
from speak_ukrainian.src.base import BaseComponent
from ...pages.all_news_page import AllNewsPage


class HeaderComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._club_container = None
        self._news_container = None
        self._challenge_container = None
        self._about_us_container = None
        self._service_container = None
        self._add_club_button = None

    @property
    def get_news_container_locator(self) -> Locator:
        if not self._news_container:
            self._news_container = (self.locator
                                    .locator("li", has_text='Новини'))
        return self._news_container

    @property
    def get_club_container(self) -> Locator:
        if not self._club_container:
            self._club_container = (self.locator
                                    .locator("li", has_text="Гуртки"))
        return self._club_container

    @property
    def get_challenge_container(self) -> Locator:
        if not self._challenge_container:
            self._challenge_container = (self.locator
                                         .locator("li", has_text="Челендж"))
        return self._challenge_container

    @property
    def get_about_us_container(self) -> Locator:
        if not self._about_us_container:
            self._about_us_container = (self.locator
                                        .locator("li", has_text="Про нас"))
        return self._about_us_container

    @property
    def get_service_container(self) -> Locator:
        if not self._service_container:
            self._service_container = (self.locator
                                       .locator("li", has_text="Послуги"))
        return self._service_container

    @property
    def get_add_club_button(self) -> Locator:
        if not self._add_club_button:
            self._add_club_button = (self.locator
                                     .get_by_role("button", name="Додати гурток"))
        return self._add_club_button

    def click_challenge_button(self):
        self.get_challenge_container.click()

    def click_club_button(self):
        self.get_club_container.click()

    def click_news_button(self) -> AllNewsPage:
        self.get_news_container_locator.click()
        self.locator.page.wait_for_timeout(100)
        return AllNewsPage(self.locator.page)

    def click_about_us_button(self):
        self.get_about_us_container.click()

    def click_service_button(self):
        self.get_service_container.click()

    def click_add_club_button(self):
        if self.get_add_club_button.is_visible():
            self.get_add_club_button.click()
