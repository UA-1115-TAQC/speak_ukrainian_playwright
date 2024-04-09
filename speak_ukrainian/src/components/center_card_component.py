from speak_ukrainian.src.base import BaseComponent


class CenterCardComponent(BaseComponent):
    TITLE_XPATH = "//div[contains(@class,'center-title')]"
    DESCRIPTION_XPATH = "//p[contains(@class,'center-description-in-block')]"
    RATING_XPATH = "//ul[contains(@class,'center-rating')]"
    ADDRESS_XPATH = "//div[contains(@class,'address')]"
    DETAILS_BUTTONS_XPATH = "//a[contains(@class,'details-button')]"

    def __init__(self, locator):
        super().__init__(locator)
        self._title = None
        self._description = None
        self._rating = None
        self._address = None
        self._details_button = None

    @property
    def title(self):
        if not self._title:
            self._title = self.locator.locator(self.TITLE_XPATH)
        return self._title

    @property
    def description(self):
        if not self._description:
            self._description = self.locator.locator(self.DESCRIPTION_XPATH)
        return self._description

    @property
    def rating(self):
        if not self._rating:
            self._rating = self.locator.locator(self.RATING_XPATH)
        return self._rating

    @property
    def address(self):
        if not self._address:
            self._address = self.locator.locator(self.ADDRESS_XPATH)
        return self._address

    @property
    def details_button(self):
        if not self._details_button:
            self._details_button = self.locator.locator(self.DETAILS_BUTTONS_XPATH)
        return self._details_button

    def get_name_text(self):
        return self.title.text_content()

    def click_title(self):
        self.title.click()

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()