from speak_ukrainian.src.base import BaseComponent


class LocationSearchSiderElement(BaseComponent):
    SELECT_CLEAR_XPATH = "//span[contains(@class,'ant-select-clear')]"
    INPUT_CONTENT_XPATH = "//span[contains(@class,'ant-select-selection-placeholder') or contains(@class, 'ant-select-selection-item')]"
    INPUT_BOX_XPATH = "//input[@type='search']"

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def select_clear(self):
        return self.locator.locator(self.SELECT_CLEAR_XPATH)

    @property
    def input_content(self):
        return self.locator.locator(self.INPUT_CONTENT_XPATH)

    @property
    def input_box(self):
        return self.locator.locator(self.INPUT_BOX_XPATH)

    @property
    def dropdown_box(self):
        xpath = "//div[@id='" + self.input_box.get_attribute("aria-owns") + "']/following-sibling::div"
        return LocationSearchSiderDropdownElement(self.locator.page.locator(xpath))

    def get_input_value(self):
        return self.input_content.inner_text()

    def click_clear(self):
        self.select_clear.click()
        return self

    def click_dropdown(self):
        self.locator.click()
        return self

    def select_item(self, item_name):
        self.click_dropdown().dropdown_box.select_item(item_name)
        return self


class LocationSearchSiderDropdownElement(BaseComponent):
    ITEM_LIST_XPATH = "//div[@class ='rc-virtual-list-holder-inner']/div[contains(@class, 'ant-select-item')]"

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def item_list(self):
        return self.locator.locator(self.ITEM_LIST_XPATH).all()

    def select_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            item.click()

    def find_item(self, item_name):
        while True:
            goal_item = self.find_in_list(item_name)
            if goal_item:
                return goal_item

            current_last_element_name = self.item_list[len(self.item_list) - 1].get_attribute("title")
            self.item_list[len(self.item_list) - 1].hover()
            self.locator.page.keyboard.down("ArrowDown")
            new_last_element_name = self.item_list[len(self.item_list) - 1].get_attribute("title")
            if current_last_element_name == new_last_element_name:
                break

    def find_in_list(self, item_name):
        for item in self.item_list:
            if item.get_attribute("title") == item_name:
                return item
