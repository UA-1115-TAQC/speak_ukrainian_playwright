from typing import Self

from speak_ukrainian.src.base import BasePage
from speak_ukrainian.src.components.center_card_component import CenterCardComponent
from speak_ukrainian.src.components.club_card_component import ClubCardComponent
from playwright._impl._locator import Locator

from speak_ukrainian.src.components.edit_user_profile_popup.edit_user_profile_popup import EditUserProfilePopup

from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import AddClubPopUp
class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_profile_title = page.get_by_text("Мій профіль")
        self.user_avatar = page.locator("xpath=.//span[contains(@class, 'user-avatar')]")
        self.user_name = page.locator(".//div[@class='user-name']")
        self.user_role = page.locator(".//div[@class='user-role']")
        self.user_phone = page.locator("./descendant::div[@class='user-phone-data']")
        self.user_email = page.locator("./descendant::div[@class='user-email-data']")
        self._my_drop_down_selected_item = None
        self._my_lessons_dropdown_button = None
        self._my_centers_dropdown_button = None
        self.edit_profile_button = page.locator("xpath=//span[text()='Редагувати профіль']")
        self.add_drop_down = page.get_by_role("button", name="plus Додати")
        self._add_center_button = None
        self.edit_modal_form = page.locator("xpath=./descendant::div[contains(@class, 'ant-modal css-13m256z user-edit')]"
                                            "//div[@class='ant-modal-content']")
        self._switch_pagination = None
        self.center_cards_list = page.locator(".//div[contains(@class, 'menu-component')]")

    def click_edit_profile_button(self) -> EditUserProfilePopup:
        self.edit_profile_button.click()
        return EditUserProfilePopup(self.edit_modal_form)

    def my_drop_down_selected_item_click(self) -> Self:
        self.my_drop_down_selected_item.click()
        return self

    @property
    def my_drop_down_selected_item(self) -> Locator:
        if self._my_drop_down_selected_item is None:
            self._my_drop_down_selected_item = self.page.locator(".//div[contains(@class, 'ant-select-selector')]")
        return self._my_drop_down_selected_item

    @property
    def my_lessons_dropdown_button(self) -> Locator:
        if self._my_lessons_dropdown_button is None:
            self._my_lessons_dropdown_button = self.page.locator("//div[contains(@class, 'select-item')]//span[text("
                                                                 ")='гуртки']")
        return self._my_lessons_dropdown_button

    @property
    def my_centers_dropdown_button(self) -> Locator:
        if self._my_centers_dropdown_button is None:
            self._my_centers_dropdown_button = self.page.locator("//div[contains(@class, 'select-item')]//span[text("
                                                                 ")='центри']")
        return self._my_centers_dropdown_button

    @property
    def add_club_button(self) -> Locator:
        return self.page.locator("xpath=//div[contains(@class,'ant-dropdown')]/child::*[1]//div[text()='Додати гурток']")

    @property
    def add_center_button(self) -> Locator:
        if self._add_center_button is None:
            self._add_center_button = self.page.get_by_role("menuitem", name="Додати центр").locator("div")
        return self._add_center_button

    #todo перервірити локатор пагінації коли запрацює сайт
    @property
    def switch_pagination(self) -> Locator:
        if self._switch_pagination is None:
            self._switch_pagination = self.page.locator(".//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]")
        return self._switch_pagination

    def click_my_lessons_dropdown_button(self) -> Self:
        self.my_lessons_dropdown_button.click()
        return self

    def click_my_centers_dropdown_button(self) -> Self:
        self.my_centers_dropdown_button.click()
        return self

    def click_add_drop_down(self) -> Self:
        self.add_drop_down.click()
        return self

    def click_add_club_button(self):
        self.click_add_drop_down()
        self.add_club_button.click()
        pop_up_locator = (self.page
                          .locator('div.ant-modal-wrap')
                          .filter(has=self.page.get_by_text('Додати гурток')))
        return AddClubPopUp(pop_up_locator)

    def click_add_center_button(self) -> Self:
        self.add_center_button.click()
        return self

    def get_club_cards(self) -> list[ClubCardComponent]:
        club_cards = self.page.locator(".ant-card").all()
        return [ClubCardComponent(card) for card in club_cards]

    #todo перевірити локатор центрів коли запрацює сайт
    def get_center_cards(self) -> list[CenterCardComponent]:
        center_cards = self.page.locator(".ant-card").all()
        return [CenterCardComponent(card) for card in center_cards]