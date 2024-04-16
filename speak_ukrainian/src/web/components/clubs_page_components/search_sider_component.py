from speak_ukrainian.src.web.base import BaseComponent
from speak_ukrainian.src.web.elements import LocationSearchSiderElement


class SearchSiderComponent(BaseComponent):
    CENTER_OR_CLUB_RADIO_BUTTON_XPATH = "//label[contains(@class,'ant-radio-wrapper')]"
    CHECKED_RADIO_BUTTON_XPATH = "//span[contains(@class,'ant-radio-checked')]/following-sibling::span"
    SEARCH_LOCATION_XPATH = "//div[contains(@class,'ant-select-in-form-item')]"
    ONLINE_CHECKBOX_FIELD_XPATH = "//div[@id='basic_isOnline']"
    ONLINE_CHECKBOX_INPUT_XPATH = "//div[@id='basic_isOnline']//span[contains(@class, 'ant-wave-target')]"
    DIRECTION_CHECKBOX_FIELD_LIST_XPATH = "//div[@id='basic_categoriesName']//label[contains(@class,'ant-checkbox-wrapper')]"
    DIRECTION_CHECKBOX_INPUT_LIST_XPATH = "//div[@id='basic_categoriesName']//input"
    AGE_INPUT_XPATH = "//span[@id='basic_age']//input[contains(@class,'ant-input-number-input')]"

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def center_or_club_radio_button(self):
        return self.locator.locator(self.CENTER_OR_CLUB_RADIO_BUTTON_XPATH).all()

    @property
    def checked_radio_button(self):
        return self.locator.locator(self.CHECKED_RADIO_BUTTON_XPATH)

    @property
    def search_city_box(self):
        return LocationSearchSiderElement(self.locator.locator(self.SEARCH_LOCATION_XPATH).nth(0))

    @property
    def search_district_box(self):
        return LocationSearchSiderElement(self.locator.locator(self.SEARCH_LOCATION_XPATH).nth(1))

    @property
    def search_metro_box(self):
        return LocationSearchSiderElement(self.locator.locator(self.SEARCH_LOCATION_XPATH).nth(2))

    @property
    def online_checkbox_field(self):
        if self.is_element_present(self.ONLINE_CHECKBOX_FIELD_XPATH):
            return self.locator.locator(self.ONLINE_CHECKBOX_FIELD_XPATH)

    @property
    def online_checkbox_input(self):
        if self.is_element_present(self.ONLINE_CHECKBOX_FIELD_XPATH):
            return self.locator.locator(self.ONLINE_CHECKBOX_FIELD_XPATH)

    @property
    def direction_checkbox_field_list(self):
        if self.is_element_present(self.DIRECTION_CHECKBOX_FIELD_LIST_XPATH):
            return self.locator.locator(self.DIRECTION_CHECKBOX_FIELD_LIST_XPATH).all()

    @property
    def direction_checkbox_input_list(self):
        if self.is_element_present(self.DIRECTION_CHECKBOX_INPUT_LIST_XPATH):
            return self.locator.locator(self.DIRECTION_CHECKBOX_INPUT_LIST_XPATH).all()

    @property
    def age_input(self):
        if self.is_element_present(self.AGE_INPUT_XPATH):
            return self.locator.locator(self.AGE_INPUT_XPATH)

    def is_element_present(self, xpath_name):
        return self.page.locator(xpath_name)

    def choose_club_radio_button(self):
        for e in self.center_or_club_radio_button:
            if e.text_content() == "Гурток":
                e.check()

    def choose_center_radio_button(self):
        for e in self.center_or_club_radio_button:
            if e.text_content() == "Центр":
                e.check()

    def check_online_checkbox(self):
        self.online_checkbox_input.check()

    def is_online_checkbox_checked(self):
        return self.online_checkbox_input.is_checked()

    def check_direction_checkbox(self, direction):
        for d in self.direction_checkbox_field_list:
            if d.text_content() == direction:
                d.check()

    def is_direction_checked(self, direction):
        for d in self.direction_checkbox_field_list:
            if d.text_content() == direction:
                return d.is_checked()
        return False

    def enter_age(self, age):
        self.age_input.fill(age)

    def get_age_value(self):
        return self.age_input.input_value()

    def clear_age(self):
        return self.age_input.clear()