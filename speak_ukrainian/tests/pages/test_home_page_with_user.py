from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.home_page import HomePage


def test_header_footer_visible(page_with_user: HomePage):
    (expect(page_with_user.header.locator, 'Header must be visible')
     .to_be_visible())
    (expect(page_with_user.footer.locator, 'Footer must be visible')
     .to_be_visible())
