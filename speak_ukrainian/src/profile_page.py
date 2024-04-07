from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.edit_user_profile_popup.edit_user_profile_popup import EditUserProfilePopup


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_profile_title = page.get_by_text("Мій профіль")
        self.edit_profile_button = page.locator("xpath=//span[text()='Редагувати профіль']")
        self.drop_down = page.get_by_role("button", name="plus Додати")
        self.add_club_button = page.locator("//div[contains(@class,'ant-dropdown')]/child::*[1]//div[text()='Додати центр']")
        self.add_center_button = page.get_by_role("menuitem", name="Додати центр").locator("div")
        self.edit_profile_modal_form = (page.locator("div.ant-modal css-13m256z user-edit")
                                        .and_(page.locator("div.ant-modal-content")))

    def edit_profile_button_click(self) -> EditUserProfilePopup:
        self.edit_profile_button.click()
        return EditUserProfilePopup(self.edit_profile_modal_form)

    def drop_down_click(self) -> None:
        self.drop_down.click()

    def add_club_button_click(self) -> None:
        self.add_club_button.click()

    def add_center_button_click(self) -> None:
        self.add_center_button.click()
