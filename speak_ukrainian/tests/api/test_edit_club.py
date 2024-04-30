import copy

import allure
import pytest
from playwright.sync_api import APIRequestContext

from speak_ukrainian.src.api.club_client import ClubClient
from speak_ukrainian.src.api.schames.club import ClubResponseSchema, ClubResponse
from speak_ukrainian.src.api.schames.contacts import ContactDataResponse, ContactType
from speak_ukrainian.src.api.schames.login import SingInResponse


invalid_contacts_data = [(ContactDataResponse(ContactType(1, 'Телефон'),
                                              '05045636583653'), 546),
                         (ContactDataResponse(ContactType(4, 'Пошта'),
                                              'fjhujkdj@@ha.com'), 546)]


@pytest.fixture
def tear_down_club(api_context_with_manager, request) -> (APIRequestContext, SingInResponse, ClubResponse):
    context, model = api_context_with_manager
    test_club_id = 546
    schema = ClubResponseSchema()

    club_client = ClubClient(context, token=model.access_token)
    club_response = club_client.get_club_by_id(test_club_id)
    test_club = schema.load(club_response.json())

    # Function to clear the resources
    def clear_resource():
        club_client.update_club(test_club_id, test_club)

    request.addfinalizer(clear_resource)

    return context, model, test_club


@allure.issue("TUA-977")
@allure.description('[API] Vefiry that user cannot save \'Контакти\' fields'
                    ' with invalid data (for club that is not in the center)')
@allure.label("owner", "Olena Stankevych")
@pytest.mark.parametrize('invalid_contact, club_id', invalid_contacts_data)
def test_edit_club_contacts_with_incorrect_data(tear_down_club,
                                                invalid_contact,
                                                club_id):
    context, model, club = tear_down_club
    schema = ClubResponseSchema()
    test_club = copy.deepcopy(club)
    club_client = ClubClient(context, token=model.access_token)

    test_club.contacts = [invalid_contact]
    club_client.update_club(club_id, test_club)
    club_response = club_client.get_club_by_id(club_id)
    test_club = schema.load(club_response.json())
    assert not (invalid_contact in test_club.contacts,
                f'Club should not contain \'{invalid_contact.contactData}\'')
