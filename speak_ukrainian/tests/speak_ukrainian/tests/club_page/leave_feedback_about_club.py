from playwright._impl._page import Page
from playwright.sync_api import expect

from speak_ukrainian.src.pages.club_page import ClubPage
from speak_ukrainian.src.pages.clubs_page import ClubsPage
from speak_ukrainian.src.pages.home_page import HomePage


def test_leave_comment_about_club(page_with_user: Page, page):
    COMMENT = "Some comment in comments"
    RATING = 4
    HomePage(page).header.click_club_button()
    clubs_page = ClubsPage(page)
    clubs_page.get_club_card_list()[0].click_details_button()
    club_page = ClubPage(page)
    leave_comment = club_page.click_leave_comment_button()
    leave_comment.rate_the_club(RATING)
    leave_comment.fill_comment_input(COMMENT)
    leave_comment.click_submit_button()

    (expect(club_page.get_comment[0], 'Comment should be on a list').to_contain_text(COMMENT))
