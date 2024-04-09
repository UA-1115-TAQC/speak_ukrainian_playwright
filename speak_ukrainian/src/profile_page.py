from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.edit_user_profile_popup.edit_user_profile_popup import EditUserProfilePopup


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_profile_title = page.get_by_text("Мій профіль")
        self.user_avatar = page.locator("xpath=.//span[contains(@class, 'user-avatar')]")
        self.user_name = page.locator(".//div[@class='user-name']")
        self.user_role = page.locator(".//div[@class='user-role']")
        self.user_phone = page.locator("./descendant::div[@class='user-phone-data']")
        self.user_email = page.locator("./descendant::div[@class='user-email-data']")
        self.my_drop_down_selected_item = page.locator(".//div[contains(@class, 'ant-select-selector')]")
        self.my_lessons_dropdown_button = page.locator("//div[contains(@class, 'select-item')]//span[text()='гуртки']")
        self.my_centers_dropdown_button = page.locator("//div[contains(@class, 'select-item')]//span[text()='центри']")
        self.edit_profile_button = page.locator("xpath=//span[text()='Редагувати профіль']")
        self.add_drop_down = page.get_by_role("button", name="plus Додати")
        self.add_club_button = page.locator("//div[contains(@class,'ant-dropdown')]/child::*[1]//div[text()='Додати центр']")
        self.add_center_button = page.get_by_role("menuitem", name="Додати центр").locator("div")
        self.edit_profile_modal_form = (page.locator("div.ant-modal css-13m256z user-edit")
                                        .and_(page.locator("div.ant-modal-content")))
        self.edit_modal_form = page.locator("./descendant::div[contains(@class, 'ant-modal css-13m256z user-edit')]//div["
                                            "@class='ant-modal-content']")
        self.club_cards_list = page.locator(".//div[contains(@class,'ant-card-body')]")
        self.switch_pagination = page.locator(".//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]")
        self.center_cards_list = page.locator(".//div[contains(@class, 'menu-component')]")

    def click_edit_profile_button(self) -> EditUserProfilePopup:
        self.edit_profile_button.click()
        return EditUserProfilePopup(self.edit_profile_modal_form)

    def my_drop_down_selected_item_click(self) -> None:
        self.my_drop_down_selected_item.click()

    def my_lessons_dropdown_button_click(self) -> None:
        self.my_lessons_dropdown_button.click()

    def my_centers_dropdown_button_click(self) -> None:
        self.my_centers_dropdown_button.click()

    def add_drop_down_click(self) -> None:
        self.add_drop_down.click()

    def add_club_button_click(self) -> None:
        self.add_club_button.click()

    def add_center_button_click(self) -> None:
        self.add_center_button.click()

    # todo по лісту розібратись як його формувати коли буде елемент ClubCard

    # def get_club_cards(self):
    #     club_cards = []
    #     elements = self.club_cards_list.query_selector_all(".//div[contains(@class,'ant-card-body')]")
    #     for element in elements:
    #         club_cards.append(ClubCard(element))
    #     return club_cards
