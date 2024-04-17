import logging
import os
import time

import pytest
from playwright._impl._fetch import APIRequestContext
from playwright._impl._page import Page
from playwright.sync_api import sync_playwright

from speak_ukrainian.src.api.login_client import LoginClient
from speak_ukrainian.src.api.user_client import UserClient

LOGGER = logging.getLogger(__name__)

#
# @pytest.fixture
# def page():
#     with sync_playwright() as pw:
#         browser = pw.chromium.launch(headless=False)
#         context = browser.new_context(ignore_https_errors=True)
#         page = context.new_page()
#         page.goto("http://speak-ukrainian.eastus2.cloudapp.azure.com/dev")
#         yield page
#
#         # time.sleep(10)


#
# def test_example(page: Page):
#     # page.locator(".user-profile").click()
#     # page.get_by_text("Увійти").click()
#     # page.get_by_label("Емейл").type(text="aaaa", delay=0.3)
#     # page.get_by_role("textbox", name="* Пароль:").fill("ppp")
#     # page.get_by_role("button", name="Увійти").click()
#     page.get_by_role("link", name="Гуртки", exact=True).click()
#     # page.locator(".ant-card").first.click()
#     page.locator(".ant-card").first.click()
#     for l in page.locator(".ant-card").all():
#         text = l.locator(".description").text_content()
#         LOGGER.info(text)  # page.get_by_text("Ми вивчаємо все, що можна уявити в ІТ і навіть більше. Загалом ми вчимо 20").click()  # page.get_by_text("Ми вивчаємо все, що можна уявити в ІТ і навіть більше. Загалом ми вчимо 20").click()

token = ""
def test_example1(api_context):
    lc = LoginClient(api_context)
    resource = lc.singin(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])
    assert resource.ok
    response_body = resource.json()
    assert response_body.get("email") == os.environ["USER_EMAIL"]
    global token
    token = response_body["accessToken"]

def test_example2(api_context):
    uc = UserClient(api_context, token=token)
    resource_user = uc.get_user(19)
    assert resource_user.ok
    assert resource_user.json() == {'email': '7dbcf3770c@emailaoa.pro',
                                    'firstName': 'Tester', 'id': 19,
                                    'lastName': 'TesteR',
                                    'password': '$2a$10$pMQWZdjqTFaJMip3i9fgQOOGLwYZBbbc5j1/Qg/iEriFb9DcK2QtK',
                                    'phone': '3809643849',
                                    'roleName': 'ROLE_MANAGER',
                                    'status': 'true',
                                    'urlLogo': None}


