from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


class HeaderComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def get_news_container_locator(self) -> Locator:
        return self.locator.locator("li", has_text='Новини')

    #  Як повернути news page, якщо в компоненті немає Page
    def click_news_button(self):
        self.get_news_container_locator.click()
