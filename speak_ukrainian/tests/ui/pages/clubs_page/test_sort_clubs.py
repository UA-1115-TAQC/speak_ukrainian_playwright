import allure
import pytest
from speak_ukrainian.src.web.pages.clubs_page import ClubsPage
from speak_ukrainian.src.web.pages.home_page import HomePage


@pytest.fixture(autouse=True)
def open_clubs_page(page):
    HomePage(page).advanced_search_header_component.click_advanced_search_icon()


@allure.issue("TUA-239")
@allure.description("[Розширений пошук] Verify that clubs can be sorted alphabetically (ascending)")
def test_sort_clubs_alphabetically_ascending(page):
    club_name_list = get_club_name_list(page)
    sorted_list = sorted(club_name_list)
    assert club_name_list == sorted_list


@allure.issue("TUA-239")
@allure.description("[Розширений пошук] Verify that clubs can be sorted alphabetically (descending)")
def test_sort_clubs_alphabetically_descending(page):
    clubs_page = ClubsPage(page)
    clubs_page.list_control.click_arrow_up()
    club_name_list = get_club_name_list(page)
    sorted_list = sorted(club_name_list, reverse=True)
    assert club_name_list == sorted_list


def get_club_name_list(page):
    names = []
    while True:
        clubs_page = ClubsPage(page)
        cards = clubs_page.card_list
        for card in cards:
            names.append(card.get_name_text())

        pagination = clubs_page.pagination
        if not pagination or pagination.is_next_disabled():
            break

        pagination.click_next()
    return names
