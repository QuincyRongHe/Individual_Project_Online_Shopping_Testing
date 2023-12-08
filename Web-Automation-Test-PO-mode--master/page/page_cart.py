import page
from base.base import Base
from base.get_logger import GetLogger

log = GetLogger().get_logger()

class PageCart(Base):
    def page_open_index(self):
        self.base_index()

    def page_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    def page_click_add_cart_info(self):
        self.base_click(page.cart_add_info)

    def page_click_add_cart(self):
        self.base_click(page.cart_add)

    def page_get_text(self):
        self.base_click(page.cart_see_result)
        return self.base_get_text(page.cart_add_result)

    def page_add_cart(self):
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()
