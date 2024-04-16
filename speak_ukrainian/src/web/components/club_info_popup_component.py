import re
from speak_ukrainian.src.web.base import BasePopUp
from speak_ukrainian.src.web.elements.contact_element import ContactElement
from speak_ukrainian.src.web.elements import DirectionElement


class ClubInfoPopup(BasePopUp):
    TITLE_XPATH = "//div[contains(@class, 'title')]"
    DIRECTIONS_XPATH = "//span[contains(@class,'ant-tag')]"
    RATING_XPATH = "//ul[contains(@class,'ant-rate')]"
    ADDRESS_XPATH = "//div[@class = 'address']"
    AGE_SIDER_LABEL_XPATH = "//div[@class = 'age']//span[contains(@class, 'sider-label')]"
    AGE_YEARS_XPATH = "//span[@class = 'years']"
    CONTACTS_XPATH = "//div[contains(@class,'contact')]"
    DETAILS_BUTTONS_XPATH = "//button[contains(@class,'more-button')]"
    DESCRIPTION_XPATH = "//div[contains(@class, 'about')]//div[@class = 'description']"
    FEEDBACK_XPATH = "//span[contains(@class,'feedback')]"
    DOWNLOAD_BUTTONS_XPATH = "//button[contains(@class,'download-button')]"

    def __init__(self, locator):
        super().__init__(locator)
        self._title = None
        self._direction_list = None
        self._rating = None
        self._address = None
        self._age_sider_label = None
        self._age_years = None
        self._contact_list = None
        self._details_button = None
        self._description = None
        self._feedback = None
        self._download_button = None

    @property
    def title(self):
        if not self._title:
            self._title = self.locator.locator(self.TITLE_XPATH)
        return self._title

    @property
    def direction_list(self):
        if not self._direction_list:
            directions = self.locator.locator(self.DIRECTIONS_XPATH).all()
            self._direction_list = [DirectionElement(direction) for direction in directions]
        return self._direction_list

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
    def age_sider_label(self):
        if not self._age_sider_label:
            self._age_sider_label = self.locator.locator(self.AGE_SIDER_LABEL_XPATH)
        return self._age_sider_label

    @property
    def age_years(self):
        if not self._age_years:
            self._age_years = self.locator.locator(self.AGE_YEARS_XPATH)
        return self._age_years

    @property
    def contact_list(self):
        if not self._contact_list:
            contacts = self.locator.locator(self.CONTACTS_XPATH).all()
            self._contact_list = [ContactElement(contact) for contact in contacts]
        return self._contact_list

    @property
    def details_button(self):
        if not self._details_button:
            self._details_button = self.locator.locator(self.DETAILS_BUTTONS_XPATH)
        return self._details_button

    @property
    def description(self):
        if not self._description:
            self._description = self.locator.locator(self.DESCRIPTION_XPATH)
        return self._description

    @property
    def feedback(self):
        if not self._feedback:
            self._feedback = self.locator.locator(self.FEEDBACK_XPATH)
        return self._feedback

    @property
    def download_button(self):
        if not self._download_button:
            self._download_button = self.locator.locator(self.DOWNLOAD_BUTTONS_XPATH)
        return self._download_button

    def directions_contains(self, text):
        for direction in self.direction_list:
            if text.lower() in direction.get_name_text().lower():
                return True
        return False

    def description_contains(self, text):
        return text.lower() in self.description.text_content().lower()

    def get_age_list(self):
        pattern = 'від\\s+(\\d+)\\s+до\\s+(\\d+)\\s+років'
        matcher = re.search(pattern, self.age_years.inner_text())
        if matcher:
            return [int(matcher.group(1)), int(matcher.group(2))]
        return []

    def click_details_button(self):
        self.details_button.click()
