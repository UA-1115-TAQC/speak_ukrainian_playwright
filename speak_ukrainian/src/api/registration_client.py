from playwright._impl._fetch import APIResponse

from speak_ukrainian.src.api.base_client import BaseClient


class RegistrationClient(BaseClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.path = "api/signup"

    def signup(self, email, firstName, lastName, phone, password, roleName) -> APIResponse:
        body = {
            "email": email,
            "firstName": firstName,
            "lastName": lastName,
            "phone": phone,
            "password": password,
            "roleName": roleName
        }
        response = self.request_context.post(url=self.path, data=body)
        return response
