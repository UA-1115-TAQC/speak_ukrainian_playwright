from playwright._impl._locator import Locator

from speak_ukrainian.src.components.add_center_popup.add_center_popup_component import AddCenterPopUp
from speak_ukrainian.src.components.add_center_popup.add_center_step_one import AddCenterStepOne
from speak_ukrainian.src.components.add_center_popup.add_center_step_three import AddCenterStepThree
from speak_ukrainian.src.components.add_center_popup.add_center_step_two import AddCenterStepTwo
from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import Sider
from speak_ukrainian.src.components.add_club_popup.locations_list_element import LocationsListElement


class EditCenterStepOne(AddCenterStepOne):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def add_location_button(self) -> Locator:
        return self.locator.locator("span.add-club-location")

    @property
    def locations_list(self) -> list[Locator]:
        return self.locator.locator("li.ant-list-item").all()

    @property
    def locations_list_elements(self) -> list[LocationsListElement]:
        return [LocationsListElement(location) for location in self.locations_list]

    def get_locations_name_list(self) -> list[str]:
        return [location.location_title.text_content() for location in self.list_of_location_elements]

    def click_next_step_button(self) -> 'EditCenterStepTwo':
        self.next_step_button.click()
        return EditCenterStepTwo(self.locator)


class EditCenterStepTwo(AddCenterStepTwo):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    def click_previous_step_button(self) -> EditCenterStepOne:
        self.previous_step_button.click()
        return EditCenterStepOne(self.locator)

    def click_next_step_button(self) -> 'EditCenterStepThree':
        self.next_step_button.click()
        return EditCenterStepThree(self.locator)


class EditCenterStepThree(AddCenterStepThree):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    def click_previous_step_button(self) -> EditCenterStepTwo:
        self.previous_step_button.click()
        return EditCenterStepTwo(self.locator)

    def click_complete_button(self) -> None:
        self.next_step_button.click()


class EditCenterPopUp(AddCenterPopUp):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def sider_element(self) -> Sider:
        return Sider(self.locator.locator("div.side"))

    @property
    def step_one_container(self) -> EditCenterStepOne:
        return EditCenterStepOne(self.step_container)

    @property
    def step_two_container(self) -> EditCenterStepTwo:
        return EditCenterStepTwo(self.step_container)

    @property
    def step_three_container(self) -> EditCenterStepThree:
        return EditCenterStepThree(self.step_container)
