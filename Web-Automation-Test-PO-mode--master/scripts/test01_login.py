import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
from tool.read_txt import read_txt
from base.get_logger import GetLogger


log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        parts = data.strip().split(",")
        if parts and len(parts) == 4:
            arrs.append(tuple(parts))
    return arrs


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = GetDriver().get_driver()
            cls.login = PageLogin(cls.driver)
            cls.login.page_click_login_link()
        except Exception as e:
            log.error("Error：{}".format(e))
            cls.login.base_get_image()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect_result, status):
        try:
            self.login.page_login(username, pwd)
            if status == "true":
                try:
                    self.assertTrue(self.login.page_if_login_success())
                except Exception as e:
                    self.login.base_get_image()
                    log.error("Error：{}".format(e))
                    raise
                self.login.page_click_logout_link()
                self.login.page_click_login_link()
            else:
                msg = self.login.page_get_error_info()
                print("msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    self.login.base_get_image()
                    log.error("Error：{}".format(e))
                    raise
        except Exception as e:
            log.error("Error：{}".format(e))
            self.login.base_get_image()
            raise
