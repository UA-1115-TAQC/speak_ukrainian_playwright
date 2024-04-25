import allure
import pytest

from speak_ukrainian.src.api.registration_client import RegistrationClient


invalid_data = [
    ("", "Когут", "youremail", "Kvitka1989@", "0971151309", "ROLE_MANAGER", "\"firstName\" can`t be empty"),
    ("Ігор", "", "youremail", "Kvitka1989@", "0971151309", "ROLE_MANAGER", "\"lastName\" can`t be empty"),
    ("Ігор", "Когут", "", "Kvitka1989@", "0971151309", "ROLE_MANAGER", "\"email\" can`t be empty"),
    ("Ігор", "Когут", "youremail", "", "0971151309", "ROLE_MANAGER", "\"password\" can`t be empty"),
    ("Ігор", "Когут", "youremail", "Kvitka1989@", "", "ROLE_MANAGER", "\"phone\" can`t be empty"),
    ("Ігор", "Когут", "youremail", "Kvitka1989@", "0971151309", "", "\"roleName\" can`t be empty")
    ]


@allure.issue("TUA-420")
@allure.description("[API.Реєстрація] Verify that a user with empty mandatory fields can`t be created")
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


@allure.issue("TUA-377")
@allure.description("[API] Verify that user is not registered if at least one of the mandatory fields is empty")
@pytest.mark.parametrize("firstName, lastName, email, password, phone, roleName, expected_message", invalid_data)
def test_user_is_not_created_with_empty_required_field(api_context,
                                                       firstName,
                                                       lastName,
                                                       email,
                                                       password,
                                                       phone,
                                                       roleName,
                                                       expected_message):
    user = RegistrationClient(api_context)
    resource = user.signup(firstName, lastName, email, password, phone, roleName)
    assert resource is not True

    response_body = resource.json()
    assert response_body["message"] == expected_message
