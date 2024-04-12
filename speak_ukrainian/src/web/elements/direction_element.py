from speak_ukrainian.src.web.base import BaseComponent


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
