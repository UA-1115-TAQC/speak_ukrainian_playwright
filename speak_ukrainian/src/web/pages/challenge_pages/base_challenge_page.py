from playwright.sync_api import Page, expect

from speak_ukrainian.src.web.base import BasePageWithAdvancedSearch
from speak_ukrainian.src.web.pages.payment.payment_page import Payment

CHALLENGE_IMAGE_PATH = "//div[contains(@class,\"banner\")]"
HELP_BUTTON_PATH = "//div[contains(@class,\"help-button\")]"
SOCIAL_MEDIA_PATH = "//div[contains(@class,\"social-info\")]"
CHALLENGE_IMAGE_TEACH_IN_UKR_PATH = " //div[contains(@class,\"title\") and not(contains(@role,\"menuitem\"))]"


class BaseChallengePage(BasePageWithAdvancedSearch):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def challenge_image(self):
        return self.page.locator(CHALLENGE_IMAGE_PATH)

    @property
    def challenge_image_text(self):
        return self.page.locator(CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"title\")]")

    @property
    def challenge_description_container(self):
        return self.page.locator("//div[contains(@class,\"challenge-description\")]")

    @property
    def help_project_button(self):
        return self.page.locator(HELP_BUTTON_PATH + "//button")

    @property
    def contacts_text(self):
        return self.page.locator(SOCIAL_MEDIA_PATH + "//span[contains(@class,\"text\")]")

    @property
    def contacts_social_media_icons(self):
        return self.page.locator(SOCIAL_MEDIA_PATH + "//div[contains(@class,\"links\")]/a").all()

    @property
    def signup_for_a_challenge_button(self):
        return self.page.locator("//div[contains(@class,\"button-box\")]//button")

    @property
    def signup_for_a_challenge_button_tooltip(self):
        return self.page.locator("//div[contains(@class,\"ant-tooltip-inner\")]")

    def click_sign_up_for_a_challenge_button(self):
        self.signup_for_a_challenge_button.click()

    def get_social_media_icon_by_index(self, index):
        if 0 <= index < len(self.contacts_social_media_icons):
            return self.contacts_social_media_icons[index]
        raise ValueError("The index must be between 0 and "
                         + str(len(self.contacts_social_media_icons) - 1) + ", inclusive.")

    def click_social_media_icon_by_index(self, index):
        previous_tab_amount = len(self.get_tab_handles())
        self.get_social_media_icon_by_index(index).click()
        expect(len(self.get_tab_handles()) > previous_tab_amount)
        new_tab_index = len(self.get_tab_handles()) - 1
        self.get_tab_handles()[new_tab_index].bring_to_front()

    def click_help_project_button(self):
        previous_tab_amount = len(self.get_tab_handles())
        self.help_project_button.click()
        expect(len(self.get_tab_handles()) > previous_tab_amount)
        new_tab_index = len(self.get_tab_handles()) - 1
        self.get_tab_handles()[new_tab_index].bring_to_front()
        return Payment(self.page)


class ChallengeTeachInUkrainian(BaseChallengePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def challenge_image_text(self):
        return self.page.locator(CHALLENGE_IMAGE_TEACH_IN_UKR_PATH + "/span[contains(@class,\"text\")]")

    @property
    def challenge_image_text_content(self):
        return self.page.locator(CHALLENGE_IMAGE_TEACH_IN_UKR_PATH + "/span[contains(@class,\"content\")]")


class ChallengeUkrainianClubSpeakPage(BaseChallengePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)


class ChallengeUnited(BaseChallengePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
