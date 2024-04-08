from speak_ukrainian.src.components.carousel.basic_carousel import BasicCarouselComponent
from speak_ukrainian.src.components.carousel.carousel_img_card import CarouselImgCard

IMG_SLICK_SLIDE_XPATH = ".//div[contains(@class,\"slick-slide\")]"


class CarouselImgComponent(BasicCarouselComponent):
    def __init__(self, locator) -> None:
        super().__init__(locator)
        self._switching_carousel_img_cards: dict[int, CarouselImgCard] = {}
        self._active_carousel_img_card = None

    @property
    def switching_carousel_img_cards(self) -> dict[int, CarouselImgCard]:
        if not self._switching_carousel_img_cards:
            img_cards = self.slider_container.locator.locator(IMG_SLICK_SLIDE_XPATH).all()
            for img_card in img_cards:
                data_index = int(img_card.get_attribute("data-index"))
                if 0 <= data_index <= 2:
                    self._switching_carousel_img_cards[data_index] = CarouselImgCard(img_card)
        return self._switching_carousel_img_cards

    def active_carousel_img_card(self):
        data_index = self.find_active_carousel_img_card_index()
        if not self._active_carousel_img_card:
            self._active_carousel_img_card = self.get_carousel_img_card_by_data_index(data_index)
        else:
            old_card = self._active_carousel_img_card
            old_card.card_heading.is_hidden()
            self._active_carousel_img_card = self.get_carousel_img_card_by_data_index(data_index)
        return self._active_carousel_img_card

    def get_carousel_img_card_by_data_index(self, data_index: int):
        if 0 <= data_index < len(self._switching_carousel_img_cards):
            img_card = self._switching_carousel_img_cards[data_index]
            img_card.card_heading.is_visible()
            return img_card
        raise ValueError("The index must be in the range from 0 to "
                         + str(len(self._switching_carousel_img_cards) - 1) + ", inclusive.")

    def find_active_carousel_img_card_index(self) -> int:
        for i, card in self._switching_carousel_img_cards.items():
            class_attribute = str(card.locator.get_attribute("class"))
            if class_attribute and "active" in class_attribute.split():
                return i
        return 0

    def hover_over_card_button(self, i: int):
        self.get_carousel_img_card_by_data_index(i).card_button.hover()
