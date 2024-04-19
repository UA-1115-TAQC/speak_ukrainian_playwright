from speak_ukrainian.src.api.registration_client import RegistrationClient


# TUA-420
# [API.Реєстрація] Verify that a user with empty mandatory fields can`t be created
def test_user_can_not_be_created_with_empty_fields(api_context):
    user = RegistrationClient(api_context)
    resource = user.signup("",
                           "",
                           "",
                           "",
                           "",
                           ""
    )
    assert resource is not True

    response_body = resource.json()
    assert response_body["message"] == "\"firstName\" can`t be empty"
