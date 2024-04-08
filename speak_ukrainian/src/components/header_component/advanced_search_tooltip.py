from speak_ukrainian.src.base import BaseComponent

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
    async def categories(self) -> dict:
        if not self._categories:
            self._categories = {}
            category_elements = await self.locator.locator(CATEGORY_XPATH).all()
            for category_element in category_elements:
                title = await category_element.get_attribute("title")
                self._categories[title] = category_element
        return self._categories

    @property
    async def clubs(self) -> dict:
        if not self._clubs:
            self._clubs = {}
            club_elements = await self.locator.locator(CLUB_XPATH).all()
            for club_element in club_elements:
                title = await club_element.get_attribute("title")
                self._clubs[title] = club_element
        return self._clubs

    async def get_club_by_title(self, title: str):
        clubs = await self.clubs
        return clubs.get(title)

    async def get_category_by_title(self, title: str):
        categories = await self.categories
        return categories.get(title)

    async def click_club_by_title(self, title: str):
        club_element = await self.get_club_by_title(title)
        if club_element:
            await club_element.click()

    async def click_category_by_title(self, title: str):
        category_element = await self.get_category_by_title(title)
        if category_element:
            await category_element.click()
