from speak_ukrainian.src.api.user_client import UserClient


# TUA-375
# [API]Verify if registered user can see personal data
def test_registered_user_can_see_personal_data(api_context_with_admin):
    context, model = api_context_with_admin
    uc = UserClient(context, token=model.access_token)
    resource_user = uc.get_user(model.id)
    assert resource_user.ok

    response_body = resource_user.json()
    assert response_body['id'] == 1
    assert response_body['firstName'] == 'Admin'
    assert response_body['lastName'] == 'Admin'
    assert response_body['phone'] == '0671234567'
    assert response_body['email'] == 'admin@gmail.com'
    assert response_body['roleName'] == 'ROLE_ADMIN'
    assert response_body['urlLogo'] == '/static/images/user/avatar/user1.png'
    assert response_body['status'] == 'true'
