from speak_ukrainian.src.base import BaseComponent

LOGO_XPATH = "//div[@class='title']//img"
NAME_XPATH = "//div[contains(@class,'name')]"
DIRECTIONS_XPATH = "//span[contains(@class,'ant-tag')]"
DIRECTION_LOGO_XPATH = "//div[contains(@class,'icon')]"
DIRECTION_NAME_XPATH = "//span[contains(@class,'name')]"
DESCRIPTION_XPATH = "//p[contains(@class,'description')]"
RATING_XPATH = "//ul[contains(@class,'rating')]"
ADDRESS_XPATH = "//div[contains(@class,'address')]"
DETAILS_BUTTONS_XPATH = "//*[contains(@class,'details-button')]"
# POPUP_XPATH = "//div[@class='ant-modal-root css-1kvr9ql']"
# CLUB_INFO_POPUP_ROOT_XPATH = "//div[contains(@class,'clubInfo')]"


class ClubCardComponent(BaseComponent):

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def logo(self):
        return self.locator.locator(LOGO_XPATH)

    @property
    def name(self):
        return self.locator.locator(NAME_XPATH)

    @property
    def direction_list(self):
        directions = self.locator.locator(DIRECTIONS_XPATH).all()
        return [DirectionElement(direction) for direction in directions]

    @property
    def description(self):
        return self.locator.locator(DESCRIPTION_XPATH)

    @property
    def rating(self):
        return self.locator.locator(RATING_XPATH)

    @property
    def address(self):
        return self.locator.locator(ADDRESS_XPATH)

    @property
    def details_button(self):
        return self.locator.locator(DETAILS_BUTTONS_XPATH)

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

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def logo(self):
        return self.locator.locator(DIRECTION_LOGO_XPATH)

    @property
    def name(self):
        return self.locator.locator(DIRECTION_NAME_XPATH)

    def get_name_text(self):
        return self.name.text_content()
