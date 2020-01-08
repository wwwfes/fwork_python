from selenium import webdriver
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

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers()
ff.test()