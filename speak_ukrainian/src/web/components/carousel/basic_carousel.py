from speak_ukrainian.src.web.base import BaseComponent
from playwright.sync_api import ElementHandle

LEFT_ARROW_BUTTON_XPATH = ".//span[contains(@aria-label, 'arrow-left')]"
RIGHT_ARROW_BUTTON_XPATH = ".//span[contains(@aria-label, 'arrow-right')]"
SLICK_DOTS_XPATH = ".//ul[contains(@class,\"slick-dots\")]/li"
SLICK_DOTS_CONTAINER_XPATH = ".//ul[contains(@class,\"slick-dots\")]"
SLIDER_CONTAINER_XPATH = ".//div[contains(@class,\"slick-slider\")]"


class BasicCarouselComponent(BaseComponent):
    def __init__(self, locator) -> None:
        super().__init__(locator)

    @property
    def left_arrow_button(self):
        return self.locator.locator(LEFT_ARROW_BUTTON_XPATH)

    @property
    def right_arrow_button(self):
        return self.locator.locator(RIGHT_ARROW_BUTTON_XPATH)

    @property
    def slider_container(self):
        return self.locator.locator(SLIDER_CONTAINER_XPATH)

    @property
    def slick_dots_container(self):
        return self.locator.locator(SLICK_DOTS_CONTAINER_XPATH)

    @property
    def slick_dots(self):
        return self.locator.locator(SLICK_DOTS_XPATH).all()

    def click_left_arrow_button(self):
        self.left_arrow_button.click()

    def click_right_arrow_button(self):
        self.right_arrow_button.click()

    def click_slick_dot_by_index(self, index):
        slick_dot = self.get_slick_dot_by_index(index)
        slick_dot.click()
        try:
            self.wait_for_selector(
                f"(//ul[contains(@class,'slick-dots')]/li)[{index + 1}][@style='background-color: rgb(250, 140, 22)']"
            )
        except Exception as e:
            print(f"Error occurred: {e}")

    def get_slick_dot_by_index(self, index) -> ElementHandle:
        if 0 <= index < len(self.slick_dots):
            return self.slick_dots[index]
        raise ValueError("The index must be in the range between 0 and " + str((len(self.slick_dots) - 1))
                         + ", inclusive")

    def get_active_slick_dot(self):
        for dot in self.slick_dots:
            if "slick-active" in dot.get_attribute("class"):
                return dot

    def click_active_slick_dot(self):
        active_dot = self.get_active_slick_dot()
        if active_dot:
            active_dot.click()
        return self

    def get_slick_dot_color(self, slick_dot: ElementHandle) -> str:
        return slick_dot.evaluate("el => window.getComputedStyle(el).backgroundColor")
