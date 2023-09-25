import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from .pages.login_page import LoginPage
import faker




def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")
    
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='function')
def create_new_user(browser):
    f = faker.Faker()
    login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.register_new_user(email = f.email(), password = 'QWEqwe123!')
    login_page.should_be_authorized_user()