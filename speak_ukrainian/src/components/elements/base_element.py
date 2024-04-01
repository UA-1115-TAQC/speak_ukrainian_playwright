from speak_ukrainian.src.base import BasePage


class BaseElement(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def get_value_css_properties(self, locator, property_name):
        return locator.evaluate('(element) => window.getComputedStyle(element).getPropertyValue(arguments[0])',
                                property_name)