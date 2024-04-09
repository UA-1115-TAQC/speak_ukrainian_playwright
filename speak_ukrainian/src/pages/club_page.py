from playwright._impl._locator import Locator
from playwright._impl._page import Page

from speak_ukrainian.src.base import BasePage


class ClubPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.write_to_manager = None
        self.sign_up_to_club = None
        self.leave_comment = None
        self.show_more_comment = None

    @property
    def sign_up_to_club_button(self) -> Locator:
        if not self.sign_up_to_club:
            self.sign_up_to_club = (self.page.get_by_role("button", name="Записатись на гурток"))
            return self.sign_up_to_club



    def click_sign_up_club_button(self) -> AddCenterStepTwo:
        self.sign_up_to_club_button.click()
        return AddCenterStepTwo(self.locator)
