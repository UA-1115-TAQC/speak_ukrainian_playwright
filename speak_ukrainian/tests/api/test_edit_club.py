import allure
import pytest

from speak_ukrainian.src.api.club_client import ClubClient
from speak_ukrainian.src.api.schames.club import ClubResponseSchema
from speak_ukrainian.src.api.schames.contacts import ContactDataResponse, ContactType

invalid_contacts_data = [(ContactDataResponse(ContactType(1, 'Телефон'),
                                              '05045636583653'), 546),
                         (ContactDataResponse(ContactType(4, 'Пошта'),
                                              'fjhujkdj@@ha.com'), 546)]


@allure.issue("TUA-977")
@allure.description('[API] Vefiry that user cannot save \'Контакти\' fields'
                    ' with invalid data (for club that is not in the center)')
@pytest.mark.parametrize('invalid_contact, club_id', invalid_contacts_data)
def test_edit_club_contacts_with_incorrect_data(api_context_with_manager,
                                                invalid_contact,
                                                club_id):
    context, model = api_context_with_manager
    schema = ClubResponseSchema()

    club_client = ClubClient(context, token=model.access_token)
    club_response = club_client.get_club_by_id(club_id)
    test_club = schema.load(club_response.json())

    test_club.contacts = [invalid_contact]
    club_client.update_club(club_id, test_club)
    club_response = club_client.get_club_by_id(club_id)
    test_club = schema.load(club_response.json())
    assert not (invalid_contact in test_club.contacts,
                f'Club should not contain \'{invalid_contact.contactData}\'')
