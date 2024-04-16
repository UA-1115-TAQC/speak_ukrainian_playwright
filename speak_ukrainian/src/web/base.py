from playwright.sync_api import expect, Page, Locator


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
        super().__init__(page)
        self.page = page

    @property
    def header(self) -> 'HeaderComponent':
        from speak_ukrainian.src.web.components.header_component.header_component import HeaderComponent
        return HeaderComponent(self.page.locator(HEADER_XPATH))

    @property
    def footer(self) -> 'FooterComponent':
        from speak_ukrainian.src.web.components.footer_component import FooterComponent
        return FooterComponent(self.page.locator(FOOTER_XPATH))

    @property
    def get_top_notice_message(self):
        return self.page.locator(TOP_NOTICE_MESSAGE_XPATH)


class BasePageWithAdvancedSearch(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def advanced_search_header_component(self) -> 'AdvancedSearchHeaderComponent':
        from speak_ukrainian.src.web.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
        return AdvancedSearchHeaderComponent(self.page.locator(ADVANCED_SEARCH_HEADER_XPATH))


class BaseComponent:
    def __init__(self, locator: Locator):
        self.locator = locator

    def wait_to_be_visible(self, element: Locator) -> Locator:
        element.scroll_into_view_if_needed()
        expect(element).to_be_visible()
        return element

    def wait_for_selector(self, selector, timeout=30):
        for _ in range(timeout):
            if self.locator.is_selector_present(selector):
                return True
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


class BaseCarousel(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._left_arrow_button = None
        self._right_arrow_button = None
        self._slick_dots = None
        self._carousel_container = None

    @property
    def get_left_arrow_button(self) -> Locator:
        if not self._left_arrow_button:
            self._left_arrow_button = (self.locator
                                       .locator("span[aria-label='arrow-left']"))
        return self._left_arrow_button

    @property
    def get_right_arrow_button(self) -> Locator:
        if not self._right_arrow_button:
            self._right_arrow_button = (self.locator
                                        .locator("span[aria-label='arrow-right']"))
        return self._right_arrow_button

    @property
    def get_slick_dots(self) -> Locator:
        if not self._slick_dots:
            self._slick_dots = (self.locator
                                .locator("ul.slick-dots > li"))
        return self._slick_dots

    @property
    def get_carousel_container(self) -> Locator:
        if not self._carousel_container:
            self._carousel_container = (self.locator
                                        .locator("div.slick-slider"))
        return self._carousel_container

    def click_slick_dot_by_index(self, index: int):
        self.get_slick_dots.nth(index).click()

    def get_active_slick_dot(self) -> Locator:
        for dot in self.get_slick_dots.all():
            if dot.get_attribute("class") == "slick-active":
                return dot
        return None
