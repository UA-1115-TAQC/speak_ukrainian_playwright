class Input:
    def __init__(self, page):
        self.page = page

    def input(self):
        return self.page.locator("[class*='input']")

    def set_input_value(self, input_value, selector_name) -> None:
        placeholder = self.input().locator(selector_name).first
        placeholder.fill(input_value)

    def get_input_value(self, selector_name) -> str:
        input_element = self.input().locator(selector_name).first
        return input_element.get_attribute("value")
