from speak_ukrainian.src.base import BaseComponent


class ListControlComponent(BaseComponent):
    ARROW_UP_XPATH = "//span[contains(@aria-label, 'arrow-up')]"
    ARROW_DOWN_XPATH = "//span[contains(@aria-label, 'arrow-down')]"
    WRAPPER_LIST_XPATH = "//label[contains(@class, 'ant-radio-button-wrapper')][1]"
    WRAPPER_BLOCK_XPATH = "//label[contains(@class, 'ant-radio-button-wrapper')][2]"

    def __init__(self, locator):
        super().__init__(locator)
        self._sort_by_alphabet = None
        self._sort_by_rating = None
        self._arrow_up = None
        self._arrow_down = None
        self._wrapper_list = None
        self._wrapper_block = None

    @property
    def sort_by_alphabet(self):
        if not self._sort_by_alphabet:
            self._sort_by_alphabet = self.locator.get_by_text("за алфавітом")
        return self._sort_by_alphabet

    @property
    def sort_by_rating(self):
        if not self._sort_by_rating:
            self._sort_by_rating = self.locator.get_by_text("за рейтингом")
        return self._sort_by_rating

    @property
    def arrow_up(self):
        if not self._arrow_up:
            self._arrow_up = self.locator.locator(self.ARROW_UP_XPATH)
        return self._arrow_up

    @property
    def arrow_down(self):
        if not self._arrow_down:
            self._arrow_down = self.locator.locator(self.ARROW_DOWN_XPATH)
        return self._arrow_down

    @property
    def wrapper_list(self):
        if not self._wrapper_list:
            self._wrapper_list = self.locator.locator(self.WRAPPER_LIST_XPATH)
        return self._wrapper_list

    @property
    def wrapper_block(self):
        if not self._wrapper_block:
            self._wrapper_block = self.locator.locator(self.WRAPPER_BLOCK_XPATH)
        return self._wrapper_block

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
