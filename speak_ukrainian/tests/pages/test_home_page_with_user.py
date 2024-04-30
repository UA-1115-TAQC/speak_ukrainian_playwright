import allure
from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.home_page import HomePage


@allure.issue('TUA-868')
@allure.description('Verify that the header and the footer are visible')
@allure.label("owner", "Olena Stankevych")
def test_header_footer_visible(page_with_user: HomePage):
    (expect(page_with_user.header.locator, 'Header must be visible')
     .to_be_visible())
    (expect(page_with_user.footer.locator, 'Footer must be visible')
     .to_be_visible())
