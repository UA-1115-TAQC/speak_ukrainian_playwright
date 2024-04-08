import asyncio

import playwright
from playwright._impl._locator import Locator
from playwright._impl._page import Page
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page


class BaseComponent:
    def __init__(self, locator: Locator):
        self.locator = locator

    def wait_to_be_visible(self, element: Locator) -> Locator:
        element.scroll_into_view_if_needed()
        expect(element).to_be_visible()
        return element

    async def wait_for_selector(self, selector, timeout=30):
        for _ in range(timeout):
            if await self.locator.is_selector_present(selector):
                return True
            await asyncio.sleep(1)
        return False

class BasePopUp(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._close_button = None

    def is_open(self) -> bool:
        return self.locator.is_visible()

    @property
    def close_button(self) -> Locator:
        if self._close_button is None:
            self._close_button = self.locator.get_by_label("Close", exact=True)
        return self._close_button

    def click_close_button(self) -> None:
        self.close_button.click()
