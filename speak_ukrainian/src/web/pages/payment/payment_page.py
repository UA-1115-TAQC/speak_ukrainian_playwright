from playwright.sync_api import Page

from speak_ukrainian.src.web.base import BasePageWithoutHeaderAndFooter

INITIATIVE_HEADER_PATH = "//div[contains(@class,\"header\")]"
INITIATIVE_DESCRIPTION_PATH = "//div[contains(@class,\"description\")]"


class Payment(BasePageWithoutHeaderAndFooter):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def large_logo_image(self):
        return self.page.locator(INITIATIVE_HEADER_PATH + "//div[contains(@class,\"large\")]")

    @property
    def initiative_title(self):
        return self.page.locator(INITIATIVE_HEADER_PATH + "//div[contains(@class,\"title\")]")

    @property
    def initiative_description(self):
        return self.page.locator(INITIATIVE_DESCRIPTION_PATH + "//p[not (contains(text(),\"http\"))]")

    @property
    def initiative_video_link_text(self):
        return self.page.locator(INITIATIVE_DESCRIPTION_PATH + "//p[contains(text(),\"http\")]")
