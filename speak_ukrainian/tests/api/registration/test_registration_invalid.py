import allure
import pytest
from speak_ukrainian.src.api.base_client import BaseClient


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
    response = rc.signup("bitoj41392@nubenews.com",
                         first_name,
                         "Kukh",
                         "0123456789",
                         "T12345678/",
                         "ROLE_MANAGER"
                         )
    assert response.status == 400
    assert response.json()["message"] == error_msg


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
    response = rc.signup("bitoj41392@nubenews.com",
                         "Nastia",
                         last_name,
                         "0123456789",
                         "T12345678/",
                         "ROLE_MANAGER"
                         )
    assert response.status == 400
    assert response.json()["message"] == error_msg


# def signup(first_name, last_name, base_client):
#     body = {
#         "email": "bitoj41392@nubenews.com",
#         "firstName": first_name,
#         "lastName": last_name,
#         "phone": "0123456789",
#         "password": "T12345678/",
#         "roleName": "ROLE_MANAGER"
#     }
#     context = base_client.request_context
#     return context.post(url=base_client.path, data=body)


class RegistrationClient(BaseClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.path = "api/signup"

    def signup(self, email, firstName, lastName, phone, password, roleName):
        body = {
            "email": email,
            "firstName": firstName,
            "lastName": lastName,
            "phone": phone,
            "password": password,
            "roleName": roleName
        }
        return self.request_context.post(url=self.path, data=body)

