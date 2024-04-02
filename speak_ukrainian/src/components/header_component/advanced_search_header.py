from speak_ukrainian.src.base import BaseComponent


class AdvancedSearchHeaderComponent(BaseComponent):
    def __init__(self, locator):
        super().__init__(locator)
        self._advanced_search_icon = None

    @property
    def advanced_search_icon(self):
        if not self._advanced_search_icon:
            self._advanced_search_icon = self.locator.get_by_title("Розширений пошук")
        return self._advanced_search_icon

    def click_advanced_search_icon(self):
        self.advanced_search_icon.click()


class AdvancedSearchClubsHeaderComponent(AdvancedSearchHeaderComponent):

    def __init__(self, locator):
        super().__init__(locator)
        self._show_on_map_button = None

    @property
    def show_on_map_button(self):
        if not self._show_on_map_button:
            self._show_on_map_button = self.locator.get_by_text("Показати на мапі")
        return self._show_on_map_button

    def click_show_on_map_button(self):
        self.show_on_map_button.click()
