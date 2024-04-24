import os

import pytest
from playwright.sync_api import expect

from speak_ukrainian.src.web.pages.admin_generate_certificate_page import AdminGenerateCertificatePage
from speak_ukrainian.src.web.pages.home_page import HomePage


@pytest.mark.parametrize("input_value, expected_value", [
    ("1000", "999"),
    ("1300", "999"),
    ("0", "1")
])
def test_invalid_certificates_get_tool_tip(page_with_admin: HomePage, input_value, expected_value):
    generate_certificate_page = page_with_admin.header.open_admin_menu().click_content().open_certificates_submenu_popup().click_generate_certificate()
    enter_invalid_value(generate_certificate_page, input_value)
    generate_certificate_page.study_duration_label.click()
    expect(generate_certificate_page).wait_for_selector(f'input[value!="{input_value}"]')
    updated_value = generate_certificate_page.study_duration_input.get_attribute('value')
    assert updated_value is not None and expected_value in updated_value, \
        f"The duration input accepts an invalid value {input_value}"


def enter_invalid_value(page_with_admin: AdminGenerateCertificatePage, value):
    current_value = page_with_admin.study_duration_input.get_attribute('value')
    if current_value:
        page_with_admin.study_duration_input.fill('')
    page_with_admin.study_duration_input.fill(value)
