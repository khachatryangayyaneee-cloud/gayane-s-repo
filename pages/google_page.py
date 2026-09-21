from lib.helpers import Helper
import config


class GooglePage(Helper):

    def open_google_page(self):
        try:
            self.go_to_page(config.google_url, new_window=True)
            self.switch_window(1)
            self.test_logger.info('Opened Google page')
        except Exception as e:
            self.test_logger.error(f'Open google page failed: {e}')
            raise