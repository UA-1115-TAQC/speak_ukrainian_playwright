from speak_ukrainian.src.pages.clubs_page import ClubsPage
from speak_ukrainian.src.pages.home_page import HomePage


# TUA-863
def test_direction_carousel_clickable_block_and_button(page_with_user):
    page_with_user.scroll_to_carousel_card_component_web_element()
    cards_num = len(page_with_user.carousel_card_component.carousel_cards)

    for index in range(cards_num):

        card = get_direction_card(index, page_with_user.page)
        direction_name = card.club_card_heading.text_content()
        card.click_card()
        clubs_page = ClubsPage(page_with_user.page)
        print(clubs_page.search_sider.is_direction_checked(direction_name))
        get_back_to_home_page(page_with_user.page)

        # time.sleep(20)

        card = get_direction_card(index, page_with_user.page)
        direction_name = card.club_card_heading.text_content()
        card.click_club_card_button()
        clubs_page = ClubsPage(page_with_user.page)
        print(clubs_page.search_sider.is_direction_checked(direction_name))
        get_back_to_home_page(page_with_user.page)

        # time.sleep(20)


def get_back_to_home_page(page):
    page.go_back(3000)
    HomePage(page).wait_until_directions_carousel_is_visible()


def get_direction_card(index, page):
    home_page = HomePage(page)
    carousel = home_page.carousel_card_component
    while not carousel.check_that_the_club_direction_card_obtained_by_index_is_active(index):
        carousel = home_page.carousel_card_component.click_right_arrow_button()

        # time.sleep(20)

        home_page = HomePage(page)
    return home_page.carousel_card_component.carousel_cards[index]
