import os

from speak_ukrainian.src.api.user_client import UserClient


def test_change_role_by_user(api_context_with_user):
    context, model = api_context_with_user
    uc = UserClient(context, token=model.access_token)

    resource_user = uc.put_user(os.environ["USER_ID"],
                                "email@email.com@",
                                os.environ["USER_FIRST_NAME"],
                                os.environ["USER_LAST_NAME"],
                                os.environ["USER_PHONE"],
                                os.environ["USER_URL_LOGO"],
                                os.environ["USER_STATUS"],
                                os.environ["USER_ROLE_NAME"])

    assert resource_user is not True

    response_body = resource_user.json()
    assert response_body["message"] == "Email can`t be updated"
