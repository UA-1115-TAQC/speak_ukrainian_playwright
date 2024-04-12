from playwright.sync_api import Page, expect

from speak_ukrainian.src.web.base import BasePageWithAdvancedSearch
from speak_ukrainian.src.web.components.carousel.carousel_card_component import CarouselCardComponent
from speak_ukrainian.src.web.components.carousel.carousel_img_component import CarouselImgComponent
from speak_ukrainian.src.web.pages.challenge_pages.base_challenge_page import BaseChallengePage, \
    ChallengeUkrainianClubSpeakPage
from speak_ukrainian.src.web.pages.facebook_pages.language_sphere_facebook_page import LanguageSphereFacebookPage

CHALLENGE_DESCRIPTION_PATH = "//div[contains(@class,\"challenge-description\")]"
CAROUSEL_IMG_COMPONENT_XPATH = '//div[contains(@class,"about-carousel-block")]'
CAROUSEL_CARD_COMPONENT_XPATH = '//div[contains(@class,"categories-carousel-block")]'
CHALLENGE_IMAGE_XPATH = '//div[contains(@class,"about-challenge")]//img'
CHALLENGE_DESCRIPTION_TEXT_XPATH = CHALLENGE_DESCRIPTION_PATH + "/span"
CHALLENGE_DESCRIPTION_HEADING_XPATH = CHALLENGE_DESCRIPTION_PATH + "/h2"
CHALLENGE_FIND_OUT_MORE_BUTTON_XPATH = CHALLENGE_DESCRIPTION_PATH + "//button"
SPEAKING_CLUB_HEADING_XPATH = '//div[contains(@class,"speakingclub-description")]//h2'
SPEAKING_CLUB_IMAGE_XPATH = '//img[contains(@class,"banner-image")]'


class HomePage(BasePageWithAdvancedSearch):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def speaking_club_image(self):
        return self.page.locator(SPEAKING_CLUB_IMAGE_XPATH)

    @property
    def speaking_club_heading(self):
        return self.page.locator(SPEAKING_CLUB_HEADING_XPATH)

    @property
    def challenge_image(self):
        return self.page.locator(CHALLENGE_IMAGE_XPATH)

    @property
    def challenge_description_text(self):
        return self.page.locator(CHALLENGE_DESCRIPTION_TEXT_XPATH)

    @property
    def challenge_description_heading(self):
        return self.page.locator(CHALLENGE_DESCRIPTION_HEADING_XPATH)

    @property
    def carousel_img_component(self):
        return CarouselImgComponent(self.page.locator(CAROUSEL_IMG_COMPONENT_XPATH))

    @property
    def carousel_card_component(self):
        return CarouselCardComponent(self.page.locator(CAROUSEL_CARD_COMPONENT_XPATH))

    @property
    def challenge_find_out_more_button(self) :
        find_out_more_button = self.page.locator(CHALLENGE_DESCRIPTION_PATH + "//button")
        find_out_more_button.scroll_into_view_if_needed()
        return find_out_more_button

    def click_challenge_find_out_more_button(self):
        self.challenge_find_out_more_button.click()
        base_challenge_page = BaseChallengePage(self.page)
        base_challenge_page.challenge_image.scroll_into_view_if_needed()
        expect(base_challenge_page.challenge_image).to_be_visible()
        return base_challenge_page

    def click_speaking_club_heading(self):
        self.speaking_club_heading.click()
        challenge_ukrainian_club_speak_page = ChallengeUkrainianClubSpeakPage(self.page)
        challenge_ukrainian_club_speak_page.challenge_image_text.scroll_into_view_if_needed()
        expect(challenge_ukrainian_club_speak_page.challenge_image_text).to_be_visible()
        return challenge_ukrainian_club_speak_page

    def click_speaking_club_image(self):
        previous_tab_amount = len(self.get_tab_handles())
        self.speaking_club_heading.click()
        expect(len(self.get_tab_handles()) == (previous_tab_amount + 1))
        expect(LanguageSphereFacebookPage(self.get_tab_handles()[-1]).facebook_logo).to_be_visible()
        return LanguageSphereFacebookPage(self.get_tab_handles()[-1])

    def scroll_to_all_clubs_button(self):
        self.carousel_card_component.carousel_card_all_clubs_button.scroll_into_view_if_needed()
        return self

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()
        return self

    def scroll_to_carousel_card_component_web_element(self):
        self.carousel_card_component.slider_container.scroll_into_view_if_needed()
        return self