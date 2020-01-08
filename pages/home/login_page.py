import utilities.custom_logger as cl
#from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #    self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Me connecter"
    _email_field = "edit-login"
    _password_field = "edit-password"
    _login_button = "//*[@id='edit-submit']"
    _account_link = "//div[3][@class='item item-user']//div[@class ='block-text']"
    _Selectionner_button = "edit-submit"
    _logout_button = "Me déconnecter"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def clickSelectionner(self):
        self.elementClick(self._Selectionner_button, locatorType="id")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
    #    self.getPasswordField().send_keys(Keys.RETURN)
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@class='block-text']//span[(@class='text sgt-menu-item-text')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFaild(self):
        result = self.isElementPresent("//div[ @class ='bottom-elem-container']//span[contains(@class,'error__message') and contains (text(), 'Le champ Adresse email est requis.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("CEDEO, Sanitaire - Chauffage - Plomberie - CEsDEO")

    def logout(self):
        self.driver.get("https://cedeo.test.white.adyax-dev.com/user/logout")
        #self.elementClick(self._account_link, locatorType="xpath")
        #self.elementClick(self._logout_button, locatorType="link")

        #self.nav.navigateToUserSettings()
        #logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        #elf.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
