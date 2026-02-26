import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='chrome',
                     help='Choose browser:chrome or firefox'
    )
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru/en/fr/...')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        print('\nstart chrome')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        print('/nstart firefox')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(
            'Wrong browser_name!Should be chrome or firefox'
        )
    browser.implicitly_wait(2)
    yield browser
    print('\nclose browser')
    browser.quit()
