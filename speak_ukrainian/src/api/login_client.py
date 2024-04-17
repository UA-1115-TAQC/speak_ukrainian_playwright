from playwright._impl._fetch import APIResponse

from speak_ukrainian.src.api.base_client import BaseClient


class LoginClient(BaseClient):
    def __init__(self, request_context):
        super().__init__(request_context)
        self.path = "api/signin"

    def singin(self, email, password) -> APIResponse:
        body = {
            "email": email,
            "password": password
        }
        response = self.request_context.post(url=self.path, data=body)
        return response
