from playwright._impl._locator import Locator
from playwright._impl._page import Page

from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.sign_up_to_club_popup.sign_up_to_club import SignUpToClub
from speak_ukrainian.src.components.write_to_manager_popup.write_to_manager_component import WriteToManagerPopUp


class ClubPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.write_to_manager = None
        self.sign_up_to_club = None
        self.leave_comment = None

    @property
    def sign_up_to_club_button(self) -> Locator:
        if self.sign_up_to_club is None:
            self.sign_up_to_club = (self.page.get_by_role("button", name="Записатись на гурток"))
            return self.sign_up_to_club

    def click_sign_up_club_button(self) -> SignUpToClub:
        self.sign_up_to_club_button.click()
        return SignUpToClub(self.page.locator("div.SignUpForClub_signUpForClubModal"))

    @property
    def write_to_manager_button(self) -> Locator:
        if self.write_to_manager is None:
            self.write_to_manager = (self.page.get_by_role("button", name="Написати менеджеру"))
            return self.write_to_manager

    def click_write_to_manager_button(self) -> WriteToManagerPopUp:
        self.write_to_manager_button.click()
        return WriteToManagerPopUp(self.page.locator("div.ant-modal-content"))
