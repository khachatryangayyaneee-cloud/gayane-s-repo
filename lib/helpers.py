import logging
import os
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Helper():

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def _error_with_screenshot(self, message):
        logging.error(message)
        os.makedirs(self.test_logger.screenshot_dir, exist_ok=True)
        self.driver.save_screenshot(f"{self.test_logger.screenshot_dir}/{self.test_logger.test_name}.png")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=f"{self.test_logger.test_name}_failure",
            attachment_type=allure.attachment_type.PNG,
        )
    
    def go_to_page(self, url, new_window=False):
        try:
            if new_window:
                self.test_logger.info(f'Opening page in a new window: {url}')
                self.driver.execute_script(f"window.open('{url}');")
            else:
                self.test_logger.info(f'Opening page: {url}')
                self.driver.get(url)
        except Exception as e:
            self._error_with_screenshot(f'Go to page failed: {e}')
            raise

    def find_and_click(self, loc, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(loc)
            )
            elem.click()
            self.test_logger.info(f'Clicked element: {loc}')
        except Exception as e:
            self._error_with_screenshot(f'Find and click failed for {loc}: {e}')
            raise

    def find_and_send_keys(self, loc, inp_text, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(loc)
            )
            elem.send_keys(inp_text)
            self.test_logger.info(f'Entered text into element: {loc}')
        except Exception as e:
            self._error_with_screenshot(f'Find and send keys failed for {loc}: {e}')
            raise

    def get_text(self, loc, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(loc)
            )
            text = elem.text
            self.test_logger.info(f'Got text for element {loc}: {text}')
            return text
        except Exception as e:
            self._error_with_screenshot(f'Get text failed for {loc}: {e}')
            raise

    def get_attribute(self, loc, attribute, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(loc)
            )
            value = elem.get_attribute(attribute)
            self.test_logger.info(f'Got attribute {attribute} for element {loc}: {value}')
            return value
        except Exception as e:
            self._error_with_screenshot(f'Get attribute failed for {loc}: {e}')
            raise

    def switch_window(self, window_id=0):
        try:
            self.driver.switch_to.window(self.driver.window_handles[window_id])
            self.test_logger.info(f'Switched to window: {window_id}')
        except Exception as e:
            self._error_with_screenshot(f'Switch window failed: {e}')
            raise

    def accept_alert(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.test_logger.info(f'Accepted alert with text: {alert_text}')
            return alert_text
        except Exception as e:
            self._error_with_screenshot(f'Accept alert failed: {e}')
            raise

    def append_text_to_file(self, file_path, text):
        try:
            with open(file_path, 'a+') as f:
                f.write(text + '\n')
            self.test_logger.info(f'Appended text to file {file_path}: {text}')
        except Exception as e:
            self.test_logger.error(f'Append text to file failed for {file_path}: {e}')
            raise