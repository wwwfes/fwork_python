from pages.BO.loginlogout import LoginBODev
from pages.BO.content_site_settings_pageDev import CSSP
from utilities.teststatus import TestStatus
import unittest
import pytest
from selenium import webdriver
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginBOTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lbo = LoginBODev(self.driver)
        self.cs = CSSP(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_createNewElInMenu(self):
        self.lbo.loginBODev("vfesan", "vfesan")
        self.cs.goToCOntSitePage()
        self.cs.clearFields()
        title = "eeeeefffffeqeііііdaxesdf"
        #need to copy in 'clickOnNewEL' in '_new_created_el'
        self.cs.enterTitle(title)
        self.cs.selectUrl()
        self.cs.checkOINT()
        self.cs.clickSaveButton()
        self.lbo.logoutBODev()

        self.cs.checkOnHomePage()
        self.cs.clickProductsMenu()
        result = self.cs.verifyTitleSuccessful()
        assert result == True
        result = self.cs.verifyURLSuccessful()
        assert result == True
        self.cs.clickOnNewEL()
        time.sleep(2)

        # написать код чтоб проверил чекание чекбокса (если чекнутый - не трогать)
        # нужно еще проверить что открылось в новой вкладке

    @pytest.mark.run(order=2)
    def test_deleteNewElInMenu(self):
        self.lbo.loginBODev("vfesan", "vfesan")
        self.cs.goToCOntSitePage()
        self.cs.checkOINT()
        self.cs.clearFieldsWithTabs()
        self.cs.checkOINT()
        self.cs.clickSaveButton()

        self.cs.checkOnHomePage()
        self.cs.clickProductsMenu()
        result = self.cs.verifyTitleSuccessful()
        assert result == False
        result = self.cs.verifyURLSuccessful()
        assert result == False
        self.cs.clickOnNewEL()
        time.sleep(2)



# py.test tests/BO/BO_test.py --browser chrome