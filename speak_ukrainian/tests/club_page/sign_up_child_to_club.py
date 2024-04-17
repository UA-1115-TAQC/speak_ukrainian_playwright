import time

from playwright._impl._page import Page
from playwright.sync_api import expect

from speak_ukrainian.src.pages.club_page import ClubPage
from speak_ukrainian.src.pages.clubs_page import ClubsPage
from speak_ukrainian.src.pages.home_page import HomePage


def test_leave_comment_about_club(page_with_user: Page, page):
    COMMENT = "some comment"
    TOP_NOTICE_MESSAGE = "Запит на реєстрацію в гурток надіслано"
    HomePage(page).header.click_club_button()
    clubs_page = ClubsPage(page)
    clubs_page.get_club_card_list()[0].click_details_button()
    club_page = ClubPage(page)
    sign_up_to_club = club_page.click_sign_up_club_button()
    sign_up_to_club.click_child_checkbox_by_index(1)
    sign_up_to_club.fill_comment_input(COMMENT)
    sign_up_to_club.click_submit_button()

    (expect(HomePage(page).get_top_notice_message, 'Top notice message should be displayed').to_contain_text(TOP_NOTICE_MESSAGE))


