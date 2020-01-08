from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplicitWaitType
import time


class ExplicitWaitDemo1():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2019")
        returnData = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnData.clear()
        returnData.send_keys("19")
        driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]//label//button').click()


        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()


ff = ExplicitWaitDemo1()
ff.test()