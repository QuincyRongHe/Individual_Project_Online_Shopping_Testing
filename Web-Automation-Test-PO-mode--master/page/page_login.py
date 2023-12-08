from base.base import Base
import page
from base.get_logger import GetLogger


log = GetLogger().get_logger()


class PageLogin(Base):
    def page_click_login_link(self):
        self.base_click(page.login_link)


    def page_input_username(self, username):
        self.base_input(page.login_username, username)


    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)


    def page_click_login_btn(self):
        self.base_click(page.login_btn)


    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)


    def page_if_login_success(self):
        return self.base_element_is_exist(page.login_logout_link)


    def page_click_logout_link(self):
        self.base_click(page.login_logout_btn)
        self.base_click(page.login_logout_link)

    def page_if_logout_success(self):
        return self.base_element_is_exist(page.login_link)

    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    def page_login_success(self, username="fakeuser1@gmail.com", pwd="12345"):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()


