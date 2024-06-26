import allure
from speak_ukrainian.src.web.pages.clubs_page import ClubsPage
from speak_ukrainian.src.web.pages.home_page import HomePage


@allure.issue("TUA-863")
@allure.description("[Home page] [The user is logged in] Verify that clickable is all block and the 'Переглянути' button on the carousel with suggested clubs")
def test_direction_carousel_clickable_block_and_button(page_with_user):
    page_with_user.scroll_to_carousel_card_component_web_element()
    cards_num = len(page_with_user.carousel_card_component.carousel_cards)
    for index in range(cards_num):
        card = get_direction_card(index, page_with_user.page)
        direction_name = card.club_card_heading.text_content()
        card.click_card()
        clubs_page = ClubsPage(page_with_user.page)
        assert clubs_page.search_sider.is_direction_checked(direction_name)
        get_back_to_home_page(page_with_user.page)

        card = get_direction_card(index, page_with_user.page)
        direction_name = card.club_card_heading.text_content()
        card.click_club_card_button()
        clubs_page = ClubsPage(page_with_user.page)
        assert clubs_page.search_sider.is_direction_checked(direction_name)
        get_back_to_home_page(page_with_user.page)


def get_back_to_home_page(page):
    page.go_back()
    HomePage(page).wait_until_directions_carousel_is_visible()


def get_direction_card(index, page):
    home_page = HomePage(page)
    home_page.wait_until_directions_carousel_is_visible()
    while not home_page.carousel_card_component.check_that_the_club_direction_card_obtained_by_index_is_active(index):
        home_page.carousel_card_component.click_right_arrow_button()
        home_page = HomePage(page)
    return home_page.carousel_card_component.carousel_cards[index]
