from .pages.login_page import LoginPage


LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

def test_login_page_url(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_url()

def test_login_form(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_form()

def test_registration_form(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_register_form()
