import time
import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class TestOrder(unittest.TestCase):
    # setup
    def setUp(self):
        self.driver = GetDriver().get_driver()
        PageLogin(self.driver).page_login_success()
        self.order = PageOrder(self.driver)
        self.order.page_click_index()

    # teardown
    def tearDown(self):
        GetDriver().quit_driver()

    def test_order(self):
        try:
            self.order.page_order()
            msg = self.order.page_get_submit_result()
            print("msg:", msg)
            self.assertIn("Thank you!", msg)
        except Exception as e:
            self.order.base_get_image()
            log.error("Error：{}".format(e))
            raise

