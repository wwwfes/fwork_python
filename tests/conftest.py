import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import time

@pytest.yield_fixture()
#@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
#@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    #lp = LoginPage(driver)
    #lp.login("gcolleu-at-wanadoo.fr@yopmail.com", "password")
    #lp.clickSelectionner()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# py.test home\login_tests.py --browser firefox
# py.test home\login_tests.py --browser iexplorer
# py.test tests\home\login_tests.py --browser chrome