import unittest


from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.cart = PageCart(self.driver)
        PageLogin(self.driver).page_login_success()
        self.cart.page_open_index()

    def tearDown(self):
        GetDriver().quit_driver()

    def test_add_cart(self):
        try:
            self.cart.page_add_cart()
            msg = self.cart.page_get_text()
            self.assertEqual(msg, "TV")
        except Exception as e:
            self.cart.base_get_image()
            log.error("Error：{}".format(e))
            raise
        