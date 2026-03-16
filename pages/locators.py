from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inv')
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-group a.btn[href*="/basket/"]')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MSG = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)  .alertinner strong')
    CART_PRICE_MSG = (By.XPATH,'//div[contains(@class,"alert-info")]/div/p/strong')
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main > h1')
    PRODUCT_PRICE = (By.XPATH,'//div[contains(@class,"product_main")]/p[@class="price_color"]')

class BasketPageLocators():
    EMPTY_BASKET_MSG= (By.XPATH, '//div/p[contains(text(),"Your basket is empty")]')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
