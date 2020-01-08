from traceback import print_stack
from utilities.util import Util
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class CSSP(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    ##############
    ## Locators ##
    ##############
    _url_field = "edit-field-css-bottom-menu-item-0-uri"
    _title_field = "edit-field-css-bottom-menu-item-0-title"
    _oint_checkbox = "edit-field-css-bottom-menu-item-0-options-attributes-target"
    _save_button = "edit-submit"
    # On FO
    _produits_in_menu = "//li[@class='item item-products']//a"
    _new_created_el = "eeeeefffffeqedaxesdf"

    ##########################
    ## Element Interactions ##
    ##########################

    def goToCOntSitePage(self):
        self.driver.get("https://cedeo.dev.white.adyax-dev.com/admin/structure/config_pages/content_site_settings/edit")

    def clearFields(self):
        urlField = self.getElement(locator=self._url_field)
        urlField.clear()
        titleField = self.getElement(locator=self._title_field)
        titleField.clear()

    def clearFieldsWithTabs(self):

        titleField = self.getElement(locator=self._title_field)
        titleField.clear()
        time.sleep(5)
        urlField = self.getElement(locator=self._url_field)
        urlField.clear()
        time.sleep(5)
        urlField.send_keys(Keys.BACKSPACE)


    def enterTitle(self, text):
        self.sendKeys(text, self._title_field)

    def typeInURL(self, text):
        self.sendKeys(text, self._url_field)

    def selectUrl(self):
        urlField = self.getElement(locator=self._url_field)
        urlField.send_keys("B")
        time.sleep(3)
        urlField.send_keys(Keys.DOWN)
        urlField.send_keys(Keys.DOWN)
        urlField.send_keys(Keys.DOWN)
        urlField.send_keys(Keys.RETURN)

    def checkOINT(self):
        self.elementClick(self._oint_checkbox)


    def clickSaveButton(self):
        self.elementClick(self._save_button)


##########  on FO  #######################


    def checkOnHomePage(self):
        self.driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com")


    def clickProductsMenu(self):
        self.elementClick(self._produits_in_menu, locatorType="xpath")

    def verifyURLSuccessful(self):
        result = self.isElementPresent("//li[@class='bottom-item']//a[@href='/les-marques/bosch']",
                                       locatorType="xpath")
        return result

    def verifyTitleSuccessful(self):
        result = self.isElementPresent("eeeeefffffeqedaxesdf", locatorType="link")
        return result

    def clickOnNewEL(self):
        self.elementClick(self._new_created_el, locatorType="link")

    def newElementAbsent(self):
        self.isElementPresent("//li[@class='bottom-item']//a[@href='/les-marques/bosch']",
                                       locatorType="xpath")
        return result
