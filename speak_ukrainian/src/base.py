class BasePage:
    def __init__(self, page):
        self.page = page


class BaseComponent:
    def __init__(self, locator):
        self.locator = locator
