import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        driverLocation = "C:\\PyCharm Community Edition 2019.1.1\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        self.driver = webdriver.Chrome(driverLocation)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.clear()
        elem.send_keys("ldzushvlidjzfnvlaie7y4of8aeuifvnhluhrevlsie85ywgo9eur")
        elem.send_keys(Keys.RETURN)
        assert "No results found." in driver.page_source

    def test_cedeo(self):
        driver = self.driver
        driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/connexion")
        user = ""
        pwd = ""
        elem = driver.find_element_by_id("edit-login")
        elem.send_keys(user)
        elem = driver.find_element_by_id("edit-password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert ">Le champ Adresse email est requis.</span>" in driver.page_source
        elem.clear()
        user = "123"
        pwd = "321"
        elem = driver.find_element_by_id("edit-login")
        elem.send_keys(user)
        elem = driver.find_element_by_id("edit-password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert ">Saisissez une adresse mail valide</span>" in driver.page_source
        elem = driver.find_element_by_id("edit-login")
        elem.clear()
        elem = driver.find_element_by_id("edit-password")
        elem.clear()
        user = "12флвоупмшдкотпеыдкшорншкдпе3"
        pwd = "32укеруенруенркернке1"
        elem = driver.find_element_by_id("edit-login")
        elem.send_keys(user)
        elem = driver.find_element_by_id("edit-password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        # invalid bechavior
        assert ">Le champ Adresse email est requis.</span>" in driver.page_source
        assert ">Saisissez une adresse mail valide</span>" in driver.page_source


if __name__ == "__main__":
    unittest.main()