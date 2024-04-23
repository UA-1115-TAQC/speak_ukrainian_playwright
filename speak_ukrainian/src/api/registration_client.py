from playwright._impl._fetch import APIResponse

from speak_ukrainian.src.api.base_client import BaseClient


class RegistrationClient(BaseClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.path = "api/signup"

    def signup(self, firstName, lastName, email, password, phone, roleName) -> APIResponse:
        body = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "roleName": roleName
        }
        response = self.request_context.post(url=self.path, data=body)
        return response
