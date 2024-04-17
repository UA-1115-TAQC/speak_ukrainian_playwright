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