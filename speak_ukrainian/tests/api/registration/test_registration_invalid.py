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

invalid_registration_data = [('Nastia123', 'Kukh', 'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400, '\'firstName\' can`t contain numbers'),
                             ('Nastia#$@@', 'Kukh', 'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400,
                              '\'firstName\' can contain only ukrainian and english letters'),
                             ('Nastia', 'Kukh123', 'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400, '\'lastName\' can`t contain numbers'),
                             ('Nastia', 'Kukh##%#', 'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400,
                              '\'lastName\' can contain only ukrainian and english letters'),
                             ('NastiaNastiaNastiaNastiaNastiaNastiaNastiaNastiaNastia', 'Kukh',
                              'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400, '\'firstName\' can contain from 1 to 25 letters'),
                             ('Nastia', 'KukharKukharKukharKukharKukharKukharKukharKukharKukhar',
                              'bitoj41392@nubenews.com', 'Entermail13/',
                              '0975463923', 'ROLE_MANAGER', 400, '\'lastName\' can contain from 1 to 25 letters')]


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
    return registration_client.signup(first_name,
                                      last_name,
                                      "bitoj41392@nubenews.com",
                                      "T12345678/",
                                      "0123456789",
                                      "ROLE_MANAGER")


@allure.issue('TUA-419')
@allure.description('[API.Реєстрація] Verify that a user with non-existing role can`t be created')
@allure.label("owner", "Olena Stankevych")
def test_register_with_invalid_role(api_context):
    invalid_role_name = 'ROLE_CUSTOMER'
    expected_response_message = f'Role not found by name: {invalid_role_name}'
    expected_response_status = 404
    rc = RegistrationClient(api_context)
    response = rc.signup('User', 'User', 'test.email@ukr.net',
                         'Entermail13/', '0671234567', invalid_role_name)
    assert response.status == expected_response_status, f'Response status should be {expected_response_status}'
    assert (response.json()['message'] == expected_response_message,
            f'\'{expected_response_message}\' should be returned')


@allure.issue('TUA-423')
@allure.description('[API.Реєстрація] Verify that a user with invalid data can`t be created')
@allure.label('owner', 'Olena Stankevych')
@pytest.mark.parametrize("first_name, last_name, email, password,"
                         "phone, role, status_code, error_msg", invalid_registration_data)
def test_register_user_with_incorrect_data(api_context, first_name, last_name,
                                           email, password, phone,
                                           role, status_code, error_msg):
    rc = RegistrationClient(api_context)
    response = rc.signup(first_name, last_name, email, password, phone, role)

    assert (response.status == status_code,
            f'Response status should be \'{status_code}\'')
    assert (response.json()['message'] == error_msg,
            f'Error message should be \'{error_msg}\'')
