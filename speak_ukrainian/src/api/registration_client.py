from speak_ukrainian.src.api.base_client import BaseClient


class RegistrationClient(BaseClient):
    def __init__(self, request_context):
        super().__init__(request_context)
        self.path = "api/signup"

    def signup(self, email, first_name, last_name, phone, password, role_name, url_logo):
        response = self.request_context.post(url=self.path, data={
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "phone": phone,
            "password": password,
            "roleName": role_name,
            "urlLogo": url_logo,
        })
        return response