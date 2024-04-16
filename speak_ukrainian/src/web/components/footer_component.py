from typing import Self

from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BaseComponent


class FooterComponent (BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._logo = None
        self._motto_under_logo = None
        self._social_links = None
        self._copyright_text = None
        self._sponsors_title = None
        self._sponsors_links = None
        self._donate_title = None
        self._explanation = None
        self._donate_button = None

    @property
    def logo_img(self) -> Locator:
        if not self._logo:
            self._logo = self.locator.locator(".footer-logo")
        return self._logo

    def click_on_logo(self) -> Self:
        return self.logo_img.click()

    @property
    def motto_text(self) -> Locator:
        if not self._motto_under_logo:
            self._motto_under_logo = self.locator.locator(".description .text")
        return self._motto_under_logo

    @property
    def list_of_social_links(self) -> list[Locator]:
        return self.locator.locator(".links").all()

    def social_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_social_links] if self.list_of_social_links else []

    @property
    def copyright_text(self) -> Locator:
        if not self._copyright_text:
            self._copyright_text = self.locator.locator(".qubstudio")
        return self._copyright_text

    @property
    def sponsors_title(self) -> Locator:
        if not self._sponsors_title:
            self._sponsors_title = self.locator.locator(".footer-partners .article")
        return self._sponsors_title

    @property
    def list_of_sponsors_links(self) -> list[Locator]:
        return self.locator.locator(".sponsors").all()

    def sponsors_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_sponsors_links] if self.list_of_sponsors_links else []

    @property
    def donate_title(self) -> Locator:
        if not self._donate_title:
            self._donate_title = self.locator.locator(".footer-donate .article")
        return self._donate_title

    @property
    def explanation(self) -> Locator:
        if not self._explanation:
            self._explanation = self.locator.locator(".desc")
        return self._explanation

    @property
    def donate_button(self) -> Locator:
        if not self._donate_button:
            self._donate_button = self.locator.get_by_role("button", name="Допомогти проєкту")
        return self._donate_button

    def click_on_donate_button(self) -> Self:
        self.donate_button.click()
        return self
