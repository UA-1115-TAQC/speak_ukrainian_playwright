import allure
from speak_ukrainian.src.api.user_client import UserClient


@allure.issue("TUA-408")
@allure.description("[API. Edit profile] User can edit profile with valid data")
def test_register_with_invalid_first_names_data(api_context_with_user):
    api_context, sing_in_response = api_context_with_user
    uc = UserClient(api_context, sing_in_response.access_token)


