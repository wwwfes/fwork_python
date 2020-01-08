import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html


    def test(self):
        driverLocation = "C:\\PyCharm Community Edition 2019.1.1\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL

        driver.get("https://white:white2oi8@cedeo.test.white.adyax-dev.com/connexion")
        elem = driver.find_element_by_id("edit-login")
        elem.send_keys("belkacimi.smail@yopmail.com")
        elem = driver.find_element_by_id("edit-password")
        elem.send_keys("password")
        elem.send_keys(Keys.RETURN)

ff = RunChromeTests()
ff.test()

