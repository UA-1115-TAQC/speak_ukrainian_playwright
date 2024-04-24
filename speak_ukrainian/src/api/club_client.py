from playwright._impl._fetch import APIResponse

from speak_ukrainian.src.api.base_client import BaseClient
from speak_ukrainian.src.api.schames.club import ClubResponse, ClubResponseSchema


class ClubClient(BaseClient):
    def __init__(self, api_context, token=None):
        super().__init__(api_context, token=token)
        self.path = 'api/'

    def get_club_by_id(self, club_id) -> APIResponse:
        return self.request_context.get(url=f'{self.path}club/{club_id}',
                                        headers={'Authorization': f'Bearer {self.token}',
                                                 "Content-Type": "application/json"})

    def get_clubs_all(self) -> APIResponse:
        return self.request_context.get(url=f'{self.path}clubs',
                                        headers={'Authorization': f'Bearer {self.token}'})

    def get_list_clubs_by_user_id(self, user_id) -> APIResponse:
        return self.request_context.get(url=f'{self.path}clubs/{user_id}',
                                        headers={'Authorization': f'Bearer {self.token}'})

    def update_club(self, club_id, club_body: ClubResponse) -> APIResponse:
        schema = ClubResponseSchema()
        club_body = schema.dumps(club_body)
        return self.request_context.put(url=f'{self.path}club/{club_id}',
                                        headers={'Authorization': f'Bearer {self.token}',
                                                 "Content-Type": "application/json"}, data=club_body)
