import os
import re

import allure
from playwright.sync_api import expect
from playwright._impl._page import Page

from speak_ukrainian.src.web.components.header_component.header_component import HeaderComponent
from speak_ukrainian.src.web.pages.clubs_page import ClubsPage
from speak_ukrainian.src.web.pages.home_page import HomePage


def test_news_button_redirects_to_news_page(page: Page):
    expected_active_class = 'ant-menu-item-active'
    expected_news_path = '/news'

    header = HeaderComponent(page.get_by_role('banner'))
    (expect(header.get_news_container_locator, message='News button should not be underlined by default')
     .to_have_css('border-bottom-style', 'none'))

    header.get_news_container_locator.hover()
    style = (header.get_news_container_locator
             .evaluate("el => window.getComputedStyle(el, '::after')['border-bottom']"))
    (expect(header.get_news_container_locator, f'News container should have {expected_active_class} class')
     .to_have_class(re.compile(expected_active_class)))
    assert 'solid' in style
    assert '255, 255, 255' in style

    header = header.click_news_button().header
    (expect(page, 'News page should be opened')
     .to_have_url(re.compile(expected_news_path)))

    header = header.click_logo().header
    (expect(header.get_news_container_locator, 'News button should not be underlined')
     .not_to_have_class(re.compile(expected_active_class)))
    (expect(page, 'Home page should be opened')
     .not_to_have_url(re.compile(expected_news_path)))

def test_check_that_slick_dots_container_on_img_carousel_is_centered(page: Page):
    home_page = HomePage(page)
    assert "center" in home_page.carousel_img_component.slick_dots_container.evaluate(
        '(element) => getComputedStyle(element).justifyContent')


@allure.issue("TUA-44")
@allure.description("Verify that user can perform basic search by whole words")
def test_basic_search_in_advanced_search_header(page: Page):
    home_page = HomePage(page)
    search_queries = ["American Gymnastics Club", "Сфера"]
    for query in search_queries:
        check_that_user_can_do_basic_search_by_string(home_page, query)
        # +Check the search result with DB #todo

 
def check_that_user_can_do_basic_search_by_string(page: Page, string: str):
    string = string.strip().lower()
    advanced_search_input_field = page.locator('.advanced-search-header-component input')
    advanced_search_input_field.fill(string)
    clubs_page_url = os.environ["BASE_URL"]+"clubs"
    page.goto(clubs_page_url)
    club_cards = ClubsPage(page).get_club_card_list()
    for card in club_cards:
        name_text = card.text_content(selector='.name').strip().lower()
        description_text = card.text_content(selector='.description').strip().lower()
        tag_names = [tag.text_content().strip().lower() for tag in card.query_selector_all('.tag')]
        assert string in name_text or string in description_text or string in tag_names, \
            f"Search query '{string}' not found in club card information."
    # +Check the search result with DB #todo
