import time
import page
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger

log = GetLogger().get_logger()

class Base:

    def __init__(self, driver):
        self.driver = driver

    # Element Location Encapsulation
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # Click Encapsulation
    def base_click(self, loc):
        self.base_find(loc).click()
        # self.driver.execute_script("arguments[0].click();", self.base_find(loc))

    # Input Encapsulation
    def base_input(self, loc, value):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    # Get Text Encapsulation
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # Screenshot Encapsulation
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # Element exists or not Encapsulation
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=5)
            return True  # Element exists
        except Exception as e:
            return False  # Element does not exist

    # Return to Home Encapsulation
    def base_index(self):
        time.sleep(5)
        self.driver.get(page.URL)

    # Return to Default Directory Encapsulation
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # Switch Window Encapsulation
    def base_switch_to_window(self, title):
        self.driver.switch_to.window(self.base_get_title_handle(title))

    # Get Handle Encapsulation
    def base_get_title_handle(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                return handle
