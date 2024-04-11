from speak_ukrainian.src.base import BaseComponent

CLUB_CARD_IMAGE_XPATH = ".//div[contains(@class,\"icon-box\")]/img"
CLUB_CARD_HEADING_XPATH = ".//div[contains(@class,\"name\")]"
CLUB_CARD_TEXT_XPATH = ".//div[contains(@class,\"description\")]"
CLUB_CARD_BUTTON_XPATH = ".//div[contains(@class,\"details\")]"
CLUB_CARD_BUTTON_POINTER_XPATH = ".//span[@aria-label=\"arrow-right\"]"


class ClubDirectionCard(BaseComponent):
    def __init__(self, locator) -> None:
        super().__init__(locator)

    @property
    def club_card_image(self):
        return self.locator.locator(CLUB_CARD_IMAGE_XPATH)

    @property
    def club_card_heading(self):
        return self.locator.locator(CLUB_CARD_HEADING_XPATH)

    @property
    def club_card_text(self):
        return self.locator.locator(CLUB_CARD_TEXT_XPATH)

    @property
    def club_card_button(self):
        return self.locator.locator(CLUB_CARD_BUTTON_XPATH)

    @property
    def club_card_button_pointer(self):
        return self.locator.locator(CLUB_CARD_BUTTON_POINTER_XPATH)

    def click_card(self):
        # TODO added method
        self.club_card_heading.click()

    # ClubsPage will be returned as a result
    def click_club_card_button(self):
        self.club_card_button.click()

    # ClubsPage will be returned as a result
    def click_club_card_button_pointer(self):
        self.club_card_button_pointer.click()
