from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/connexion")
# #driver.find_element_by_xpath('//*[@id="page"]/section[1]/div/div[3]/div[2]/div[2]/a').click()
# driver.find_element_by_link_text("Produits").click()
el = driver.find_element_by_xpath("//li[@class='item item-products']//a")
el.click()

element = driver.find_element_by_link_text("eeeeefffffeqedaxesdf")
element.click()
