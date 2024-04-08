from speak_ukrainian.src.components.carousel.basic_carousel import BasicCarouselComponent
from speak_ukrainian.src.components.carousel.club_direction_card import ClubDirectionCard

CAROUSEL_CARD_HEADING_XPATH = "//div[contains(@class,\"categories-header\")]/h2"
CAROUSEL_CARD_ALL_CLUBS_BUTTON_XPATH = "//div[contains(@class,\"categories-header\")]/a/button"
CAROUSEL_CARD_XPATH = ".//div[contains(@class,\"slick-slide\")]"


class CarouselCardComponent(BasicCarouselComponent):
    def __init__(self, locator) -> None:
        super().__init__(locator)
        self._carousel_cards = None
        self._active_carousel_cards = None

    @property
    def carousel_card_heading(self):
        return self.locator.locator(CAROUSEL_CARD_HEADING_XPATH)

    @property
    def carousel_card_all_clubs_button(self):
        return self.locator.locator(CAROUSEL_CARD_ALL_CLUBS_BUTTON_XPATH)

    @property
    async def carousel_cards(self) -> list[ClubDirectionCard]:
        if not self._carousel_cards:
            cards = await self.slider_container.locator.locator(CAROUSEL_CARD_XPATH).all()
            self._carousel_cards = [ClubDirectionCard(card) for card in cards]
        return self._carousel_cards

    #ClubsPage will be returned as a result
    def click_carousel_card_all_clubs_button(self):
        self.carousel_card_all_clubs_button.click()

    async def get_club_direction_card_by_index(self, index):
        if 0 <= index <= (len(await self.carousel_cards) - 1):
            return (await self.carousel_cards)[index]
        raise ValueError(
            f"The index must be in the range between 0 and {len(await self.carousel_cards) - 1}, inclusive")

    async def check_that_the_club_direction_card_obtained_by_index_is_active(self, index) -> bool:
        return (await self.get_club_direction_card_by_index(index)).club_card_heading.is_displayed()

    async def get_active_carousel_cards(self) :
        if not self._active_carousel_cards:
            self._active_carousel_cards = await self.__filter_displayed_cards__(await self.carousel_cards)
        old_cards = self._active_carousel_cards
        try:
            await self.locator.wait_for(not old_cards[-1].is_displayed())
            self._active_carousel_cards = await self.__filter_displayed_cards__(await self.carousel_cards)
        except Exception:
            print("You are already at the beginning/end of the cards list")
        return self._active_carousel_cards

    async def __filter_displayed_cards__(self, cards) :
        return [card for card in cards if await card.club_card_heading.is_displayed()]

    async def get_active_carousel_card_by_index(self, index) :
        active_cards = await self.get_active_carousel_cards()
        if 0 <= index <= (len(active_cards) - 1):
            return active_cards[index]
        raise ValueError(f"The index must be in the range between 0 and {len(active_cards) - 1}, inclusive")
