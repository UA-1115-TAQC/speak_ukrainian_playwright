import re

from playwright.sync_api import expect
from playwright._impl._page import Page
from speak_ukrainian.src.components.header_component.header_component import HeaderComponent


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
