from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.cedeo.fr/connexion")

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
#invalid bechavior
assert ">Le champ Adresse email est requis.</span>" in driver.page_source


#elem = find_element_by_class_name("btn-clear")


#elem = driver.find_element_by_id("email")

#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)
#driver.close()
