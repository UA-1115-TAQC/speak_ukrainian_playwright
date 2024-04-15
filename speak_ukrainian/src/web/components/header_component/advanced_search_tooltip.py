from speak_ukrainian.src.web.base import BaseComponent

CATEGORY_NAME_CATEGORIES_XPATH = "//div[contains(@title,\"Категорії\")]"
CATEGORY_NAME_CLUBS_XPATH = "//div[contains(@title,\"Гуртки\")]"
CATEGORY_XPATH = "//div[@type='category']"
CLUB_XPATH = "//div[@type='club']"


class AdvancedSearchToolTip(BaseComponent):
    def __init__(self, locator):
        super().__init__(locator)
        self._categories = None
        self._clubs = None

    @property
    def categories(self) -> dict:
        if not self._categories:
            self._categories = {}
            category_elements = self.locator.locator(CATEGORY_XPATH).all()
            for category_element in category_elements:
                title = category_element.get_attribute("title")
                self._categories[title] = category_element
        return self._categories

    @property
    def clubs(self) -> dict:
        if not self._clubs:
            self._clubs = {}
            club_elements = self.locator.locator(CLUB_XPATH).all()
            for club_element in club_elements:
                title = club_element.get_attribute("title")
                self._clubs[title] = club_element
        return self._clubs

    def get_club_by_title(self, title: str):
        clubs = self.clubs
        return clubs.get(title)

    def get_category_by_title(self, title: str):
        categories = self.categories
        return categories.get(title)

    def click_club_by_title(self, title: str):
        club_element = self.get_club_by_title(title)
        if club_element:
            club_element.click()

    def click_category_by_title(self, title: str):
        category_element = self.get_category_by_title(title)
        if category_element:
            category_element.click()
