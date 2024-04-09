from speak_ukrainian.src.base import BaseComponent


class ClubCardComponent(BaseComponent):
    LOGO_XPATH = "//div[@class='title']//img"
    NAME_XPATH = "//div[contains(@class,'name')]"
    DIRECTIONS_XPATH = "//span[contains(@class,'ant-tag')]"
    DESCRIPTION_XPATH = "//p[contains(@class,'description')]"
    RATING_XPATH = "//ul[contains(@class,'rating')]"
    ADDRESS_XPATH = "//div[contains(@class,'address')]"
    DETAILS_BUTTONS_XPATH = "//*[contains(@class,'details-button')]"
    # POPUP_XPATH = "//div[@class='ant-modal-root css-1kvr9ql']"
    # CLUB_INFO_POPUP_ROOT_XPATH = "//div[contains(@class,'clubInfo')]"

    def __init__(self, locator):
        super().__init__(locator)
        self._logo = None
        self._name = None
        self._direction_list = None
        self._description = None
        self._rating = None
        self._address = None
        self._details_button = None

    @property
    def logo(self):
        if not self._logo:
            self._logo = self.locator.locator(self.LOGO_XPATH)
        return self._logo

    @property
    def name(self):
        if not self._name:
            self._name = self.locator.locator(self.NAME_XPATH)
        return self._name

    @property
    def direction_list(self):
        if not self._direction_list:
            directions = self.locator.locator(self.DIRECTIONS_XPATH).all()
            self._direction_list = [DirectionElement(direction) for direction in directions]
        return self._direction_list

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

    def get_logo_src(self):
        return self.logo.get_attribute("src")

    def get_name_text(self):
        return self.name.text_content()

    def name_contains(self, text):
        return text.lower() in self.get_name_text().lower()

    def direction_contains(self, text):
        for direction in self.direction_list:
            if text.lower() in direction.get_name_text().lower():
                return True
        return False

    def description_contains(self, text):
        return text.lower() in self.description.text_content().lower()

    def click_title(self):
        self.name.click()

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()


class DirectionElement(BaseComponent):
    DIRECTION_LOGO_XPATH = "//div[contains(@class,'icon')]"
    DIRECTION_NAME_XPATH = "//span[contains(@class,'name')]"

    def __init__(self, locator):
        super().__init__(locator)
        self._logo = None
        self._name = None

    @property
    def logo(self):
        if not self._logo:
            self._logo = self.locator.locator(self.DIRECTION_LOGO_XPATH)
        return self._logo

    @property
    def name(self):
        if not self._name:
            self._name = self.locator.locator(self.DIRECTION_NAME_XPATH)
        return self._name

    def get_name_text(self):
        return self.name.text_content()
