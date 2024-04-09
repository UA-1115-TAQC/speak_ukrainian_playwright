import logging

import pytest
from playwright._impl._page import Page
from playwright.sync_api import sync_playwright

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://speak-ukrainian.eastus2.cloudapp.azure.com/dev")
        yield page

        # time.sleep(10)



def test_example(page: Page):
    # page.locator(".user-profile").click()
    # page.get_by_text("Увійти").click()
    # page.get_by_label("Емейл").type(text="aaaa", delay=0.3)
    # page.get_by_role("textbox", name="* Пароль:").fill("ppp")
    # page.get_by_role("button", name="Увійти").click()
    page.get_by_role("link", name="Гуртки", exact=True).click()
    # page.locator(".ant-card").first.click()
    page.locator(".ant-card").first.click()
    for l in page.locator(".ant-card").all():
        text = l.locator(".description").text_content()
        LOGGER.info(text)  # page.get_by_text("Ми вивчаємо все, що можна уявити в ІТ і навіть більше. Загалом ми вчимо 20").click()  # page.get_by_text("Ми вивчаємо все, що можна уявити в ІТ і навіть більше. Загалом ми вчимо 20").click()
