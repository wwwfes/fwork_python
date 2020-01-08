import unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        driverLocation = "C:\\PyCharm Community Edition 2019.1.1\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        self.driver = webdriver.Chrome(driverLocation)
        # Open the provided URL


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://white:white2oi8@cedeo.test.white.adyax-dev.com/connexion")
        elem = driver.find_element_by_id("edit-login")
        elem.send_keys("belkacimi.smail@yopmail.com")
        elem = driver.find_element_by_id("edit-password")
        elem.send_keys("password")
        elem.send_keys(Keys.RETURN)


if __name__ == "__main__":
    unittest.main()

  