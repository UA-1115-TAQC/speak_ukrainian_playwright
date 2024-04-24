import os

import allure
from marshmallow import ValidationError

from speak_ukrainian.src.api.schames.user import UserResponseSchema
from speak_ukrainian.src.api.user_client import UserClient


@allure.issue("TUA-375")
@allure.description("[API]Verify if registered user can see personal data")
def test_registered_user_can_see_personal_data(api_context_with_admin):
    context, model = api_context_with_admin
    uc = UserClient(context, token=model.access_token)
    resource_user = uc.get_user(model.id)
    assert resource_user.ok

    response_body = resource_user.json()
    assert response_body['id'] == int(os.environ["ADMIN_ID"])
    assert response_body['firstName'] == os.environ["ADMIN_FIRST_NAME"]
    assert response_body['lastName'] == os.environ["ADMIN_LAST_NAME"]
    assert response_body['phone'] == os.environ["ADMIN_PHONE"]
    assert response_body['email'] == os.environ["ADMIN_EMAIL"]
    assert response_body['roleName'] == os.environ["ADMIN_ROLE_NAME"]
    assert response_body['urlLogo'] == os.environ["ADMIN_URL_LOGO"]
    assert response_body['status'] == os.environ["ADMIN_STATUS"]


@allure.description("Schema validation test")
def test_user_response_schema(api_context_with_admin):
    context, model = api_context_with_admin
    schema = UserResponseSchema()
    user = UserClient(context, token=model.access_token)
    resource_user = user.get_user(model.id)
    resource_user_data = resource_user.json()

    try:
        schema.load(resource_user_data)
    except ValidationError as e:
        assert False, f"Validation error: {e.messages}"
