from playwright._impl._fetch import APIResponse

from speak_ukrainian.src.api.base_client import BaseClient


class RegistrationClient(BaseClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.path = "api/signup"

    def signup(self, first_name, last_name, email, password, phone, role_name) -> APIResponse:
        body = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone,
            "roleName": role_name
        }
        return self.request_context.post(url=self.path, data=body)
