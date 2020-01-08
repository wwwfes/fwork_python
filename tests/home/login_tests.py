from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("belkacimi.smail@yopmail.com", "password")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title is Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was  successful")



    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("", "")
        result = self.lp.verifyLoginFaild()
        assert result == True
        time.sleep(2)



# py.test tests/home/login_tests.py --browser chrome