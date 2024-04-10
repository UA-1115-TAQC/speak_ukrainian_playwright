from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BasePopUp, BaseComponent
from speak_ukrainian.src.components.add_club_popup.add_club_step_one import AddClubStepOne
from speak_ukrainian.src.components.add_club_popup.add_club_step_three import AddClubStepThree
from speak_ukrainian.src.components.add_club_popup.add_club_step_two import AddClubStepTwo
from speak_ukrainian.src.elements.popup_step_element import PopUpStep


class Sider(BaseComponent):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._sider_steps_containers = None

    @property
    def sider_steps_containers(self) -> list[Locator]:
        if self._sider_steps_containers is None:
            self._sider_steps_containers = self.locator.locator("div.ant-steps-item-container").all()
        return self._sider_steps_containers

    @property
    def step_one(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_containers[0])

    @property
    def step_two(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_containers[1])

    @property
    def step_three(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_containers[2])


class AddClubPopUp(BasePopUp):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
        self._step_container = self.locator.locator("main.add-club-container")

    @property
    def sider_element(self) -> Sider:
        return Sider(self.locator.locator("aside"))

    @property
    def step_one_container(self) -> AddClubStepOne:
        return AddClubStepOne(self._step_container)

    @property
    def step_two_container(self) -> AddClubStepTwo:
        return AddClubStepTwo(self._step_container)

    @property
    def step_three_container(self) -> AddClubStepThree:
        return AddClubStepThree(self._step_container)
