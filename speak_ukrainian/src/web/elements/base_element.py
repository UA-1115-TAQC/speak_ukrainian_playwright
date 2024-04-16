from playwright.sync_api import Locator

from speak_ukrainian.src.web.base import BaseComponent


class BaseElement(BaseComponent):

    def __init__(self, locator: Locator):
        super().__init__(locator)

    def get_value_css_properties(self, locator, property_name):
        return locator.evaluate('(element) => window.getComputedStyle(element)'
                                '.getPropertyValue(arguments[0])', property_name)
