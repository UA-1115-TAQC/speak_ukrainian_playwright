from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp
from speak_ukrainian.src.components.add_center_popup.add_center_step_one import AddCenterStepOne
from speak_ukrainian.src.components.add_center_popup.add_center_step_three import AddCenterStepThree
from speak_ukrainian.src.components.add_center_popup.add_center_step_two import AddCenterStepTwo
from speak_ukrainian.src.components.add_club_popup.add_club_popup_component import AddClubSider
from speak_ukrainian.src.elements.popup_step_element import PopUpStep


class AddCenterSider(AddClubSider):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

    @property
    def step_four(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_containers[3])


class AddCenterPopUp(BasePopUp):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._step_container = None

    @property
    def step_container(self):
        if self._step_container is None:
            self._step_container = self.locator.locator("main.add-center-container")
        return self._step_container

    @property
    def sider_element(self) -> AddCenterSider:
        return AddCenterSider(self.locator.locator("div.side"))

    @property
    def step_one_container(self) -> AddCenterStepOne:
        return AddCenterStepOne(self.step_container)

    @property
    def step_two_container(self) -> AddCenterStepTwo:
        return AddCenterStepTwo(self.step_container)

    @property
    def step_three_container(self) -> AddCenterStepThree:
        return AddCenterStepThree(self.step_container)

    # @property
    # def step_four_container(self) -> AddCenterStepFour:
    #     return AddCenterStepFour(self.step_container)

    @property
    def get_active_step(self) -> Locator:
        return self.step_container.locator("div.ant-steps-item-active span.ant-steps-icon")
