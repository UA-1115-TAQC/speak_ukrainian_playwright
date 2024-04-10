from playwright.sync_api import Page

from speak_ukrainian.src.base import BasePageWithoutHeaderAndFooter

STUDY_DURATION_LABEL_XPATH = "//label[@for=\"basic_hours\"]"
STUDY_DURATION_INPUT_XPATH = "//input[@name=\"hours\"]"


class AdminGenerateCertificatePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def study_duration_label(self):
        return self.page.locator(STUDY_DURATION_LABEL_XPATH)

    @property
    def study_duration_input(self):
        return self.page.locator(STUDY_DURATION_INPUT_XPATH)
