from speak_ukrainian.src.pages.clubs_page import ClubsPage
from speak_ukrainian.src.pages.home_page import HomePage


# TUA-825
def test_clubs_change_with_entered_character(page):
    HomePage(page).header.click_club_button()
    text = ["С", "п", "о", "р", "т"]
    assert is_text_present_on_cards(page, text)


def is_text_present_on_cards(page, text):
    clubs_page = ClubsPage(page)
    input_str = ""
    for letter in text:
        input_str = input_str + letter
        clubs_page.search_clubs_header.set_text_selection_search_input_field(input_str)
        search_str = clubs_page.search_clubs_header.get_text_selection_search_input_field()
        clubs_page = ClubsPage(page)
        clubs = clubs_page.card_list
        if not check_text_on_cards(search_str, clubs):
            return False
    return True


def check_text_on_cards(search_str, clubs):
    for club in clubs:
        if club.name_contains(search_str) or club.direction_contains(search_str):
            continue
        popup = club.click_title()
        if not popup.directions_contains(search_str):
            return False
        popup.click_close_button()
    return True

