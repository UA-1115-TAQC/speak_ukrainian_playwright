import logging
import os

import pytest
from dotenv import load_dotenv
from marshmallow import ValidationError
from playwright._impl._page import Page
from playwright.sync_api import sync_playwright, Playwright, APIRequestContext

from speak_ukrainian.src.api.login_client import LoginClient
from speak_ukrainian.src.api.schames.login import SignInResponseSchema, SingInResponse
from speak_ukrainian.src.web.components.header_component.header_component import HeaderComponent
from speak_ukrainian.src.web.pages.home_page import HomePage

load_dotenv()
LOGGER = logging.getLogger(__name__)

@pytest.fixture
def page() -> Page:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=['--start-maximized'], headless=False)
        context = browser.new_context(ignore_https_errors=True, no_viewport=True)
        page = context.new_page()
        page.goto(os.environ["BASE_URL"])
        yield page


@pytest.fixture
def page_with_admin(page) -> HomePage:
    base_page = (HeaderComponent(page.get_by_role("banner"))
                 .open_guest_menu.open_login_form
                 .enter_email(os.environ["ADMIN_EMAIL"])
                 .enter_password(os.environ["ADMIN_PASSWORD"])
                 .click_sign_in_button)
    return HomePage(base_page.page)


@pytest.fixture
def page_with_manager(page) -> HomePage:
    base_page = (HeaderComponent(page.get_by_role("banner"))
                 .open_guest_menu.open_login_form
                 .enter_email(os.environ["MANAGER_EMAIL"])
                 .enter_password(os.environ["MANAGER_PASSWORD"])
                 .click_sign_in_button)
    return HomePage(base_page.page)


@pytest.fixture
def page_with_user(page) -> HomePage:
    base_page = (HeaderComponent(page.get_by_role("banner"))
                 .open_guest_menu.open_login_form
                 .enter_email(os.environ["USER_EMAIL"])
                 .enter_password(os.environ["USER_PASSWORD"])
                 .click_sign_in_button)
    return HomePage(base_page.page)


@pytest.fixture(scope="session")
def api_context() -> APIRequestContext:
    with sync_playwright() as pw:

        header = {
            # "Authorization": f"Bearer {os.environ['API_KEY']}"
        }
        request_context = pw.request.new_context(
            base_url=f'{os.environ["BASE_URL"]}',
            extra_http_headers=header
        )
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def api_context_with_user(api_context) -> (APIRequestContext, SingInResponse):
    lc = LoginClient(api_context)
    resource = lc.singin(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    schema = SignInResponseSchema()
    try:
        sing_in_response = schema.load(resource.json())
    except ValidationError as err:
        LOGGER.error(err)
    return api_context, sing_in_response

@pytest.fixture(scope="session")
def api_context_with_admin(api_context) -> (APIRequestContext, SingInResponse):
    lc = LoginClient(api_context)
    resource = lc.singin(os.environ["ADMIN_EMAIL"], os.environ["ADMIN_PASSWORD"])

    schema = SignInResponseSchema()
    try:
        sing_in_response = schema.load(resource.json())
    except ValidationError as err:
        LOGGER.error(err)
    return api_context, sing_in_response

@pytest.fixture(scope="session")
def api_context_with_manager(api_context) -> (APIRequestContext, SingInResponse):
    lc = LoginClient(api_context)
    resource = lc.singin(os.environ["MANAGER_EMAIL"], os.environ["MANAGER_PASSWORD"])

    schema = SignInResponseSchema()
    try:
        sing_in_response = schema.load(resource.json())
    except ValidationError as err:
        LOGGER.error(err)
    return api_context, sing_in_response