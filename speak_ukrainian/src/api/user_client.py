import json
from playwright._impl._fetch import APIResponse
from speak_ukrainian.src.api.base_client import BaseClient


class UserClient(BaseClient):
    def __init__(self, api_context, token):
        super().__init__(api_context, token=token)
        self.path = "api/user"

    def get_user(self, user_id) -> APIResponse:
        response = self.request_context.get(url=f"{self.path}/{user_id}",
                                            headers={"Authorization": f"Bearer {self.token}"})
        return response

    def get_users(self, role=None) -> APIResponse:
        response = self.request_context.get(url=f"{self.path}/{role if role else ""}",
                                            headers={"Authorization": f"Bearer {self.token}"})
        return response

    def put_user(self, id, email, first_name, last_name, phone, url_logo, status, role_name) -> APIResponse:
        body = {"id": id,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
                "urlLogo": url_logo,
                "status": status,
                "roleName": role_name
                }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = self.request_context.put(url=f"{self.path}/{id}", headers=headers, data=json.dumps(body))

        return response

    def put_user_with_body(self, user_id, request_body):
        response = self.request_context.put(url=f"{self.path}/{user_id}",
                                            headers={"Authorization": f"Bearer {self.token}",
                                                     "Content-Type": "application/json"},
                                            data=json.dumps(request_body))
        return response
