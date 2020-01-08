import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://white:white2oi8@https://cedeo.dev.white.adyax-dev.com/"
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://cedeo.dev.white.adyax-dev.com")
        driver.implicitly_wait(10)


if __name__ == "__main__":
    unittest.main()
