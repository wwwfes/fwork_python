from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/user/login")
elem = driver.find_element_by_id("edit-name")
elem.send_keys("vfesan")
elem = driver.find_element_by_id("edit-pass")
elem.send_keys("vfesan")
elem.send_keys(Keys.RETURN)

driver.get("https://cedeo.dev.white.adyax-dev.com/admin/structure/config_pages/content_site_settings/edit")

elem = driver.find_element(By.ID, "edit-field-css-bottom-menu-item-0-uri")
elem.send_keys("B")
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.RETURN)
elem.send_keys(Keys.BACK_SPACE)






