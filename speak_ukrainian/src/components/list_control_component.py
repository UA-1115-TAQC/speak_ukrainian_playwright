from speak_ukrainian.src.base import BaseComponent

ARROW_UP_XPATH = "//span[contains(@aria-label, 'arrow-up')]"
ARROW_DOWN_XPATH = "//span[contains(@aria-label, 'arrow-down')]"
WRAPPER_LIST_XPATH = "//label[contains(@class, 'ant-radio-button-wrapper')][1]"
WRAPPER_BLOCK_XPATH = "//label[contains(@class, 'ant-radio-button-wrapper')][2]"


class ListControlComponent(BaseComponent):

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def sort_by_alphabet(self):
        return self.locator.get_by_text("за алфавітом")

    @property
    def sort_by_rating(self):
        return self.locator.get_by_text("за рейтингом")

    @property
    def arrow_up(self):
        return self.locator.locator(ARROW_UP_XPATH)

    @property
    def arrow_down(self):
        return self.locator.locator(ARROW_DOWN_XPATH)

    @property
    def wrapper_list(self):
        return self.locator.locator(WRAPPER_LIST_XPATH)

    @property
    def wrapper_block(self):
        return self.locator.locator(WRAPPER_BLOCK_XPATH)

    def click_sort_by_alphabet(self):
        self.sort_by_alphabet.click()

    def click_sort_by_rating(self):
        self.sort_by_rating.click()

    def click_arrow_up(self):
        self.arrow_up.click()

    def click_arrow_down(self):
        self.arrow_down.click()

    def click_wrapper_list(self):
        self.wrapper_list.click()

    def click_wrapper_block(self):
        self.wrapper_block.click()
