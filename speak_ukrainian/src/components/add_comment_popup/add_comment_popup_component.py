from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp


class AddCommentPopUpComponent(BasePopUp):
    def __init__(self, locator: Locator):
        super().__init__(locator)

