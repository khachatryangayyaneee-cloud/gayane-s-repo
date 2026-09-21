import config
import pytest
from pages.practice_page import PracticePage
from pages.google_page import GooglePage
from pages.sign_in_page import SignIn

@pytest.mark.regression
def test_lets(get_driver, test_logger):

    # Create objects
    practice_page_obj = PracticePage(get_driver, test_logger)
    google_page_obj = GooglePage(get_driver, test_logger)
    sign_in_page_obj = SignIn(get_driver, test_logger)

    practice_page_obj.go_to_page(config.practice_url)
    practice_page_obj.find_and_click(practice_page_obj.btn_alert)
    alert_text = practice_page_obj.accept_alert()
    practice_page_obj.append_text_to_file(config.output_file, f'Alert text - {alert_text}')

    hide_attr = practice_page_obj.hide_element_check()
    practice_page_obj.append_text_to_file(config.output_file, f'Hidden attribute - {hide_attr}')

    practice_page_obj.mouse_hover_check()
    f_text = practice_page_obj.footer_text()
    practice_page_obj.append_text_to_file(config.output_file, f'Footer text - {f_text}')

    practice_page_obj.click_sign_in_btn()
    validation_msg = sign_in_page_obj.sign_in()
    practice_page_obj.append_text_to_file(config.output_file, f'Sign in validation message - {validation_msg}')

    google_page_obj.open_google_page()