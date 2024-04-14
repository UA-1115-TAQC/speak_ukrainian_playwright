from speak_ukrainian.src.web.base import BaseComponent

ADVANCED_SEARCH_HEADING_XPATH = "//h2[@class=\'city-name\']"
SELECTION_SEARCH_INPUT_FIELD_XPATH = '//div[contains(@class, "search")]//input[@type="search"]'
SELECTION_SEARCH_INPUT_FIELD_PLACEHOLDER_XPATH = '//span[@class=\'ant-select-selection-placeholder\']'
SEARCH_ICON_XPATH = '//div[contains(@class, "search-icon-group")]/span[@aria-label="search"]'
ADVANCED_SEARCH_TOOLTIP_NODE_XPATH = '//div[contains(@class, "rc-virtual-list-holder-inner")]'
SELECTION_SEARCH_CLOSE_BUTTON_XPATH = '//span[@aria-label="close-circle"]'


class AdvancedSearchHeaderComponent(BaseComponent):
    def __init__(self, locator):
        super().__init__(locator)

    @property
    def advanced_search_icon(self):
        return self.locator.get_by_title("Розширений пошук")

    @property
    def search_icon(self):
        return self.locator.locator(SEARCH_ICON_XPATH)

    @property
    def advanced_search_tooltip_node(self):
        return self.locator.locator(ADVANCED_SEARCH_TOOLTIP_NODE_XPATH)

    @property
    def selection_search_close_button(self):
        return self.locator.locator(SELECTION_SEARCH_CLOSE_BUTTON_XPATH)

    @property
    def advanced_search_text_heading(self):
        return self.locator.locator(ADVANCED_SEARCH_HEADING_XPATH)

    @property
    def selection_search_input_field(self):
        return self.locator.locator(SELECTION_SEARCH_INPUT_FIELD_XPATH)

    @property
    def selection_search_input_field_placeholder(self):
        return self.locator.locator(SELECTION_SEARCH_INPUT_FIELD_PLACEHOLDER_XPATH)

    def click_advanced_search_icon(self):
        self.advanced_search_icon.click()

    def get_text_selection_search_input_field(self) -> str:
        return str(self.selection_search_input_field.get_attribute("value"))

    def set_text_selection_search_input_field(self, text: str):
        self.wait_to_be_visible(self.selection_search_input_field).fill(text)
        return self

    def click_selection_search_input_field(self) -> 'AdvancedSearchToolTip':
        self.selection_search_input_field.click()
        from speak_ukrainian.src.web.components.header_component.advanced_search_tooltip import AdvancedSearchToolTip
        return AdvancedSearchToolTip(self.advanced_search_tooltip_node)

    def click_search_icon(self):
        self.search_icon.click()
        return self

    def click_selection_search_close_button(self):
        if self.get_text_selection_search_input_field() is not None:
            self.selection_search_close_button.click()
            return self
        else:
            raise ValueError("You haven't entered any text")


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
