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

    def click_slick_dot_by_index(self, index: int):
        self.get_slick_dots.nth(index).click()

    def get_active_slick_dot(self) -> Locator:
        for dot in self.get_slick_dots.all():
            if dot.get_attribute("class") == "slick-active":
                return dot
        return None
