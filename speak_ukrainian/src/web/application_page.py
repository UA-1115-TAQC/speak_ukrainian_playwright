from speak_ukrainian.src.web.base import BasePage


class ApplicationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.application_title = page.get_by_text("Заявки на розгляді")
        self.all_radio_button = page.locator("label").filter(has_text="Всі").locator("span").nth(1)
        self.not_confirm_radio_button = page.locator("label").filter(has_text="Не підтверджені").locator("span").first
        self.search_input = page.locator("label").filter(has_text="Не підтверджені").locator("span").first
        self.center_title = page.locator(".//div[contains(@class, 'noRegistrations')]")
        self.application_dropdown_selected_item = page.locator("xpath=//div[contains(@class, 'filterSelectStatuses')]//div[contains(@class, 'select-selector')]")
        self.application_dropdown_challenges_button = page.locator('#rc_select_2_list_1')

    #todo дописати клікі і сет інпут
    def all_radio_button_click(self) -> None:
        self.all_radio_button.click()