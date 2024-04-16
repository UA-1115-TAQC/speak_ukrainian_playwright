import os

from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.clubs_page import ClubsPage
from speak_ukrainian.src.web.pages.home_page import HomePage


# TUA-850
def test_search_redirect_user_to_clubs_page_from_other_pages(page_with_admin: HomePage, page):
    BASE_URL = os.environ["BASE_URL"]
    NEWS_PAGE = BASE_URL + "news"
    CLUBS_PAGE = BASE_URL + "clubs"
    CLUB_NAME = "Танці"

    all_news_page = page_with_admin.header.click_news_button()

    expect(all_news_page.page, message="News page should be loaded").to_have_url(NEWS_PAGE)

    (page_with_admin.advanced_search_header_component
                    .set_text_selection_search_input_field(CLUB_NAME)
                    .click_search_icon())

    expect(ClubsPage(page).page, message="Clubs page should be loaded").to_have_url(CLUBS_PAGE)
