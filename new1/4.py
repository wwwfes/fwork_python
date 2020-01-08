from selenium import webdriver
import pyautogui

driver = webdriver.Chrome()
driver.get("https://www.cedeo.fr/connexion")
elem = driver.find_element_by_xpath('//*[@id="sg-account-login-form"]/div[3]')
scr1 = pyautogui.screenshot()
scr1.save('screengrab.png')
elem.click()
#driver.find_element_by_id("edit-password").click()
#//*[@id="sg-account-login-form"]/div[3]