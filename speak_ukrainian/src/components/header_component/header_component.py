from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.header_component.menu.guest_menu import GuestMenu


class HeaderComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self.guest_menu_form = None

    @property
    def get_news_container_locator(self) -> Locator:
        return self.locator.locator("li", has_text='Новини')

    @property
    def profile_menu_button(self) -> Locator:
        return self.locator.locator("div.user-profile")

    #  Як повернути news page, якщо в компоненті немає Page
    def click_news_button(self):
        self.get_news_container_locator.click()

    @property
    def open_guest_menu(self) -> GuestMenu:
        self.profile_menu_button.click()
        return GuestMenu(self.locator.locator("ul.ant-dropdown-menu-light"))
