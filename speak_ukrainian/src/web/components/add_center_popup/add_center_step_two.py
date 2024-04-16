from playwright._impl._locator import Locator

from speak_ukrainian.src.web.base import BaseComponent
from speak_ukrainian.src.web.components.add_center_popup import AddCenterStepThree
from speak_ukrainian.src.web.elements import InputValidationStaticIconsAndErrors


class AddCenterStepTwo(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._popup_title = None
        self._contacts_title = None
        self._previous_step_button = None
        self._next_step_button = None

    @property
    def popup_title(self) -> Locator:
        if self._popup_title is None:
            self._popup_title = self.locator.locator("div.modal-title")
        return self._popup_title

    @property
    def contacts_title(self) -> Locator:
        if self._contacts_title is None:
            self._contacts_title = self.locator.get_by_text("Контакти", exact=True)
        return self._contacts_title

    @property
    def telephone_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#contacts_contactТелефон")))

    @property
    def facebook_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#contacts_contactFacebook")))

    @property
    def whatsapp_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#contacts_contactWhatsApp")))

    @property
    def email_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#contacts_contactПошта")))

    @property
    def skype_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.add-club-contact")
                                                   .filter(has=self.locator.page.locator("#contacts_contactSkype")))

    @property
    def site_element(self) -> InputValidationStaticIconsAndErrors:
        return InputValidationStaticIconsAndErrors(self.locator.locator("div.ant-form-item-row")
                                                    .filter(has=self.locator.page.locator("#contacts_contactSite")))

    @property
    def previous_step_button(self):
        if self._previous_step_button is None:
            self._previous_step_button = self.locator.locator("button.prev-btn")
        return self._previous_step_button

    def click_previous_step_button(self) -> 'AddCenterStepOne':
        self.previous_step_button.click()
        from speak_ukrainian.src.web.components.add_center_popup.add_center_step_one import AddCenterStepOne
        return AddCenterStepOne(self.locator)

    @property
    def next_step_button(self):
        if self._next_step_button is None:
            self._next_step_button = self.locator.locator("button.next-btn")
        return self._next_step_button

    def click_next_step_button(self) -> AddCenterStepThree:
        self.next_step_button.click()
        return AddCenterStepThree(self.locator)
