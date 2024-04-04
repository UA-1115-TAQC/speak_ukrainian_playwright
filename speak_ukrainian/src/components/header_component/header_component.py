from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.registration_popup_component.registration_popup_component import \
    RegistrationPopUpComponent


class HeaderComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def get_news_container_locator(self) -> Locator:
        return self.locator.locator("li", has_text='Новини')

    @property
    def profile_menu_button(self) -> Locator:
        return self.locator.locator("div.ant-dropdown-trigger.user-profile")

    @property
    def register_menu_button(self) -> Locator:
        return self.locator.locator("li", has_text="Зареєструватися")

    #  Як повернути news page, якщо в компоненті немає Page
    def click_news_button(self):
        self.get_news_container_locator.click()

    def click_register_button(self) -> RegistrationPopUpComponent:
        self.profile_menu_button.click()
        self.register_menu_button.click()
        return RegistrationPopUpComponent(self.locator.locator('div.ant-modal-content'))
