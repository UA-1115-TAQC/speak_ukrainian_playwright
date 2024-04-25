import allure
from speak_ukrainian.src.api.user_client import UserClient


@allure.issue("TUA-408")
@allure.description("[API. Edit profile] User can edit profile with valid data")
def test_register_with_invalid_first_names_data(api_context_with_user):
    api_context, sing_in_response = api_context_with_user
    uc = UserClient(api_context, sing_in_response.access_token)
    response = uc.get_user(sing_in_response.id)
    user_id = response.json()['id']

    request_body = make_request_body(response)
    request_body["firstName"] = "Anna"
    response = uc.put_user_with_body(user_id, request_body)
    assert response.status == 200

    request_body = make_request_body(response)
    request_body["lastName"] = "Kukarska"
    response = uc.put_user_with_body(user_id, request_body)
    assert response.status == 200

    request_body = make_request_body(response)
    request_body["phone"] = "0234567891"
    response = uc.put_user_with_body(user_id, request_body)
    assert response.status == 200


def make_request_body(response):
    response_body = response.json()
    return {"id": response_body['id'],
            "email": response_body['email'],
            "firstName": response_body['firstName'],
            "lastName": response_body['lastName'],
            "phone": response_body['phone'],
            "urlLogo": response_body['urlLogo'],
            "status": response_body['status'],
            "roleName": response_body['roleName']}


#TUA-416
def test_user_can_change_his_role(api_context_with_user):
    api_context, sing_in_response = api_context_with_user
    user_client = UserClient(api_context, sing_in_response.access_token)

    response = user_client.get_user(sing_in_response.id)
    user_id = response.json()['id']

    request_body = make_request_body(response)
    request_body["roleName"] = "ROLE_MANAGER"
    response = user_client.put_user_with_body(user_id, request_body)
    assert response.status == 200
    back_user_role(api_context_with_user)

def back_user_role(api_context_with_user):
    api_context, sing_in_response = api_context_with_user
    user_client = UserClient(api_context, sing_in_response.access_token)

    response = user_client.get_user(sing_in_response.id)
    user_id = response.json()['id']

    request_body = make_request_body(response)
    request_body["roleName"] = "ROLE_USER"
    response = user_client.put_user_with_body(user_id, request_body)
    assert response.status == 200

