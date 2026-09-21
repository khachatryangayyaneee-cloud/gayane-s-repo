from selenium.webdriver.common.by import By
from lib.helpers import Helper
from testdata import test_data


class SignIn(Helper):
    txt_email = (By.ID, "email")
    txt_pass = (By.ID, "login-password")
    btn_login = (By.ID, "login")
    msg_invalid = (By.ID, "incorrectdetails")

    def sign_in(self):
        try:
            self.find_and_send_keys(self.txt_email, test_data.email_data)
            self.find_and_send_keys(self.txt_pass, test_data.pass_data)
            self.find_and_click(self.btn_login)
            validation_msg = self.get_text(self.msg_invalid, 5)
            self.test_logger.info(f'Validation Message is - {validation_msg}')
            return validation_msg
        except Exception as e:
            self.test_logger.error(f'Sign in failed: {e}')
            raise