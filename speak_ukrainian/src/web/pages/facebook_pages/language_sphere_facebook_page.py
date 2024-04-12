from playwright.sync_api import Page

from speak_ukrainian.src.web.base import BasePageWithoutHeaderAndFooter

FACEBOOK_LOGO_XPATH = "//body//a[@aria-label=\"Facebook\"]"
INITIATIVE_HEADING_XPATH = "//body//span[contains(text(),'Сімейний фестиваль \"Мовосфера\"')]"


class LanguageSphereFacebookPage(BasePageWithoutHeaderAndFooter):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def facebook_logo(self):
        return self.page.locator(FACEBOOK_LOGO_XPATH)

    @property
    def initiative_heading(self):
        return self.page.locator(INITIATIVE_HEADING_XPATH)
