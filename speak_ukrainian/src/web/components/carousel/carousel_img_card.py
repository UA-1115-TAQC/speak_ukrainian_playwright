from speak_ukrainian.src.web.base import BaseComponent


BACKGROUND_IMAGE_XPATH = ".//div[@class=\"carousel-item\"]"
CARD_HEADING_XPATH = ".//h2"
CARD_TEXT_XPATH = ".//span[contains(@class,\"description\")]"
CARD_BUTTON_XPATH = ".//a/button"
CARD_BUTTON_TEXT_XPATH = ".//a/button/span"
CARD_LINK_XPATH = ".//a"


class CarouselImgCard(BaseComponent):
    def __init__(self, locator) -> None:
        super().__init__(locator)

    @property
    def background_image(self):
        return self.locator.locator(BACKGROUND_IMAGE_XPATH)

    @property
    def card_heading(self):
        return self.locator.locator(CARD_HEADING_XPATH)

    @property
    def card_text(self):
        return self.locator.locator(CARD_TEXT_XPATH)

    @property
    def card_button(self):
        return self.locator.locator(CARD_BUTTON_XPATH)

    @property
    def card_button_text(self):
        return self.locator.locator(CARD_BUTTON_TEXT_XPATH)

    @property
    def card_link(self):
        return self.locator.locator(CARD_LINK_XPATH)

    def get_card_link_text(self) -> str:
        return str(self.card_link.get_attribute("href"))

    def click_card_button(self):
        self.card_button.click()
