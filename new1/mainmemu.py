from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://white:white2oi8@cedeo.test.white.adyax-dev.com/connexion")
elem = driver.find_element_by_id("edit-login")
elem.send_keys("belkacimi.smail@yopmail.com")
elem = driver.find_element_by_id("edit-password")
elem.send_keys("password")
elem.send_keys(Keys.RETURN)
driver.get("https://cedeo.test.white.adyax-dev.com/p/chauffage-et-climatisation/radiateur-seche-serviettes-electrique-concerto-asymetrique-500w-A3634076")


el = driver.find_element_by_xpath('//div[@class="slider slider-nav slick-vertical slick-initialized slick-slider"]//div[@class="slick-slide slick-current slick-center"]')
el.click()
