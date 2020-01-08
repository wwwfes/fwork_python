from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():
    def test(self):
        baseurl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseurl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = UsingWrappers()
ff.test()