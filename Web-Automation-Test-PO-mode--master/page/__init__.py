from selenium.webdriver.common.by import By
URL = 'http://127.0.0.1:5000/'

"""Login"""
login_link = By.CSS_SELECTOR, "a[href='/loginForm']"
login_username = By.CSS_SELECTOR, "input[type='text']"
login_pwd = By.CSS_SELECTOR, "input[type='password']"
login_btn = By.CSS_SELECTOR, "input[type='submit']"
login_err_info = By.CSS_SELECTOR, "p"
login_logout_btn = By.CSS_SELECTOR, ".dropbtn"
login_logout_link = By.CSS_SELECTOR, "a[href='/logout']"


"""Add to Cart"""
cart_search_btn = By.CSS_SELECTOR, "a[href='/displayCategory?categoryId=3']"
cart_add_info = By.CSS_SELECTOR, "#itemImage"
cart_add = By.CSS_SELECTOR, "a[href='/addToCart?productId=13']"
cart_see_result = By.CSS_SELECTOR, ".link"
cart_add_result = By.CSS_SELECTOR, "#itemNameTag"


"""Place Order"""
order_my_cart = By.CSS_SELECTOR, "#cart"
order_account = By.CSS_SELECTOR, "a[href='/checkout']"
order_submit = By.CSS_SELECTOR, "a[href='/payment']"
order_submit_result = By.CSS_SELECTOR, "h1"
