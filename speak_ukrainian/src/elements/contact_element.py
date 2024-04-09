from speak_ukrainian.src.elements.base_element import BaseElement


class ContactElement(BaseElement):
    DIRECTION_ICON_XPATH = "//div[contains(@class,'icon')]"
    DIRECTION_NAME_XPATH = "//span[contains(@class,'contact-name')]"

    def __init__(self, node):
        super().__init__(node)
        self._icon = None
        self._name = None

    @property
    def icon(self):
        if not self._icon:
            self._icon = self.locator.locator(self.DIRECTION_ICON_XPATH)
        return self._icon

    @property
    def name(self):
        if not self._name:
            self._name = self.locator.locator(self.DIRECTION_NAME_XPATH)
        return self._name

    def click_contact(self):
        href = self.name.get_by_role("link")
        if href.is_visible():
            href.click()
