from utilities.util import Util
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginBODev(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # Locators
    _name_field = "edit-name"
    _pass_field = "edit-pass"
    _enter_button = "edit-submit"


    def goToLoginDevPage(self):
        self.driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/user/login")

    def goToLoginTestPage(self):
        self.driver.get("https://white:white2oi8@cedeo.test.white.adyax-dev.com/user/login")

    def enterNameBO(self, namebo):
        self.sendKeys(namebo, self._name_field)

    def enterPassBO(self, passwordbo):
        self.sendKeys(passwordbo, self._pass_field)

    def clickEnterButton(self):
        self.elementClick(self._enter_button)

    def loginBODev(self, name2="", password2=""):
        self.goToLoginDevPage()
        self.enterNameBO(name2)
        self.enterPassBO(password2)
        self.clickEnterButton()


    def logoutBODev(self):
        self.driver.get("https://cedeo.dev.white.adyax-dev.com/user/logout")

