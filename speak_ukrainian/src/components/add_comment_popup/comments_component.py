from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent


from speak_ukrainian.src.components.add_comment_popup.answer_to_comment_popup import AnswerToCommentPopUpComponent


class CommentsClubComponent(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self._answer_to_comment = None

    @property
    def answer_to_comment(self) -> Locator:
        if self._answer_to_comment is None:
            self._answer_to_comment = self.locator.locator("li").get_by_role("button")
            return self._answer_to_comment

    def click_on_answer_to_comment_button(self) -> AnswerToCommentPopUpComponent:
        self.answer_to_comment.click()
        return AnswerToCommentPopUpComponent(self.locator)






