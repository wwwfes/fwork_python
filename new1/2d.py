from selenium import webdriver
import selenium.webdriver.common.Keys

driver = webdriver.Chrome('c:\webdrivers\chromedriver.exe')
driver.get("http://www.python.org")

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
with mss() as sct:
    sct.shot()
driver.close()

