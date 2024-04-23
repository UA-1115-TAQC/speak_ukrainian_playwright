import allure
import pytest
from speak_ukrainian.src.api.registration_client import RegistrationClient

# TUA-423 data
invalid_first_names = [("Nastia123",
                        "\"firstName\" can`t contain numbers"),
                       ("Nastia#$@@",
                        "\"firstName\" can contain only ukrainian and english letters"),
                       ("NastiaNastiaNastiaNastiaNastiaNastiaNastiaNastiaNastia",
                        "\"firstName\" can contain from 1 to 25 letters"),
                       ]


@allure.issue("TUA-423")
@allure.description("[API.Реєстрація] Verify that a user with invalid data can`t be created.(first name)")
@pytest.mark.parametrize("first_name, error_msg", invalid_first_names)
def test_register_with_invalid_first_names_data(api_context, first_name, error_msg):
    rc = RegistrationClient(api_context)
    response = signup(first_name, "Kukh", rc)
    assert response.status == 400
    assert response.json()["message"] == error_msg


# TUA-423  data
invalid_last_names = [("Kukh123",
                       "\"lastName\" can`t contain numbers"),
                      ("Kukh##%#",
                       "\"lastName\" can contain only ukrainian and english letters"),
                      ("KukharKukharKukharKukharKukharKukharKukharKukharKukhar",
                       "\"lastName\" can contain from 1 to 25 letters"),
                      ]


@allure.issue("TUA-423")
@allure.description("[API.Реєстрація] Verify that a user with invalid data can`t be created.(last name)")
@pytest.mark.parametrize("last_name, error_msg", invalid_last_names)
def test_register_with_invalid_first_names_data(api_context, last_name, error_msg):
    rc = RegistrationClient(api_context)
    response = signup("Nastia", last_name, rc)
    assert response.status == 400
    assert response.json()["message"] == error_msg


def signup(first_name, last_name, registration_client):
    return registration_client.signup("bitoj41392@nubenews.com",
                                      first_name,
                                      last_name,
                                      "0123456789",
                                      "T12345678/",
                                      "ROLE_MANAGER",
                                      "")




