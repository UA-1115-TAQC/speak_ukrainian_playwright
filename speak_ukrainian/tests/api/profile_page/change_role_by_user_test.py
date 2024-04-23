import os

from speak_ukrainian.src.api.user_client import UserClient


def test_change_role_by_user(api_context_with_user):
    context, model = api_context_with_user
    uc = UserClient(context, token=model.access_token)

    resource_user = uc.put_user(os.environ["USER_ID"],
                                os.environ["USER_EMAIL"],
                                os.environ["USER_FIRST_NAME"],
                                os.environ["USER_LAST_NAME"],
                                os.environ["USER_PHONE"],
                                os.environ["USER_URL_LOGO"],
                                os.environ["USER_STATUS"],
                                "ROLE_MANAGER")

    assert resource_user.ok
