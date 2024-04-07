from playwright._impl._locator import Locator

from speak_ukrainian.src.base import BaseComponent
from speak_ukrainian.src.components.login_popup_component.login_popup_component import LoginPopUpComponent
from speak_ukrainian.src.components.registration_popup_component.registration_popup_component import \
    RegistrationPopUpComponent

REGISTRATION_FORM = "//div[@class='ant-modal-content']//div[@class='registration-header']/../.."
LOGIN_FORM = "//descendant::div[contains(@class, 'modal-login')][1]"


class GuestMenu(BaseComponent):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def registration(self) -> Locator:
        return self.locator.get_by_role("menuitem", name="Зареєструватися")

    @property
    def login(self) -> Locator:
        return self.locator.get_by_role("menuitem", name="Увійти")

    @property
    def open_register_form(self) -> RegistrationPopUpComponent:
        self.registration.click()
        return RegistrationPopUpComponent(self.locator.locator(REGISTRATION_FORM))

    @property
    def open_login_form(self) -> LoginPopUpComponent:
        self.login.click()
        return LoginPopUpComponent(self.locator.locator(LOGIN_FORM))
