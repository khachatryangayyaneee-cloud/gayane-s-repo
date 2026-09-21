from selenium.webdriver.common.by import By
from lib.helpers import Helper


class PracticePage(Helper):

    title = (By.XPATH, "//title[text()='Practice Page']")
    btn_alert = (By.ID, "alertbtn")
    btn_hide = (By.ID, "hide-textbox")
    inp_example = (By.ID, "displayed-text")
    btn_mousehover = (By.ID, 'mousehover')
    btn_top = (By.XPATH, "//button[@id='mousehover']//following::a[text()='Top']")
    footer = (By.XPATH, "//div[contains(@class, 'footer')]//p")
    btn_sign_in = (By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']")

    def hide_element_check(self):
        try:
            self.find_and_click(self.btn_hide)
            hide_attr = self.get_attribute(self.inp_example, 'style')
            self.test_logger.info(f'Hidden attribute is - {hide_attr}')
            return hide_attr
        except Exception as e:
            self.test_logger.error(f'Hide element check failed: {e}')
            raise

    def mouse_hover_check(self):
        try:
            self.find_and_click(self.btn_mousehover)
            self.find_and_click(self.btn_top)
            self.test_logger.info('Mouse hover check passed')
        except Exception as e:
            self.test_logger.error(f'Mouse hover check failed: {e}')
            raise

    def footer_text(self):
        try:
            f_text = self.get_text(self.footer)
            self.test_logger.info(f'Footer text is - {f_text}')
            return f_text
        except Exception as e:
            self.test_logger.error(f'Footer text check failed: {e}')
            raise

    def click_sign_in_btn(self):
        try:
            self.find_and_click(self.btn_sign_in)
            self.test_logger.info('Clicked sign in button')
        except Exception as e:
            self.test_logger.error(f'Click sign in button failed: {e}')
            raise