import asyncio

import playwright

from playwright.sync_api import expect, Page, Locator

from speak_ukrainian.src.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
from speak_ukrainian.src.components.header_component.header_component import HeaderComponent

HEADER_XPATH = "//header"
FOOTER_XPATH = "//footer"
TOP_NOTICE_MESSAGE_XPATH = ("//div[@class='ant-message-notice-wrapper']/descendant::div[contains(@class, 'ant-message-error') "
                            "or contains(@class, 'ant-message-success')]")
ADVANCED_SEARCH_HEADER_XPATH = '//div[contains(@class, "lower-header-box")]'


class BasePageWithoutHeaderAndFooter:
    def __init__(self, page: Page):
        self.page = page
        self._tab_handles = None

    def get_tab_handles(self) -> list:
        browser = self.page.context.browser
        pages = browser.contexts
        return [page for page in pages if page != self.page.context]

    def check_that_a_page_is_opened_in_a_new_tab(self, previous_handle, new_handle) -> bool:
        return previous_handle == new_handle and (len(self.get_tab_handles()) == 2)

    def switch_to_a_new_tab_by_its_index(self, index):
        tab_handles = self.get_tab_handles()
        if 0 <= index < len(tab_handles):
            tab_handles[index].bring_to_front()
        else:
            raise ValueError("The index must be in the range from 0 to " + str((len(tab_handles) - 1)) + ", inclusive")


class BasePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.page.locator(HEADER_XPATH))

    @property
    def footer(self) -> FooterComponent:
        return FooterComponent(self.page.locator(FOOTER_XPATH))


class BasePageWithAdvancedSearch(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def advanced_search_header_component(self) -> AdvancedSearchHeaderComponent:
        return AdvancedSearchHeaderComponent(self.page.locator(ADVANCED_SEARCH_HEADER_XPATH))


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
