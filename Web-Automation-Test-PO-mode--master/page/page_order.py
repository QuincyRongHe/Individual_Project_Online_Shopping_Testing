from time import sleep

import page
from base.base import Base
from base.get_logger import GetLogger


log = GetLogger().get_logger()


class PageOrder(Base):

    def page_click_index(self):
        self.base_index()

    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)


    def page_click_account(self):
        self.base_click(page.order_account)




    def page_click_submit_order(self):
        self.base_click(page.order_submit)


    def page_get_submit_result(self):
        return self.base_get_text(page.order_submit_result)


    def page_order(self):
        self.page_click_my_cart()
        self.page_click_account()
        self.page_click_submit_order()
