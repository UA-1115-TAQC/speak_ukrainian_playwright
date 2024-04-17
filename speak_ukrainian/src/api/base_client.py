from playwright._impl._fetch import APIRequestContext
from playwright.sync_api import sync_playwright


class BaseClient:
    def __init__(self, request_context, path=None, token=None):
        self.request_context = request_context
        self.path = path
        self.token = token
