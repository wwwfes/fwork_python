from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://white:white2oi8@cedeo.dev.white.adyax-dev.com/infos-agence/chevilly-la-rue-cedeo-1295")
# #driver.find_element_by_xpath('//*[@id="page"]/section[1]/div/div[3]/div[2]/div[2]/a').click()
element = driver.find_element(By.XPATH, "//*[@id='item-product-1']/div/div/ul/li[9]/a")

element.click()
driver.find_element(By.XPATH, "//div[2][@class='btn']").click()
time.sleep(2)

#PDP
driver.get("https://cedeo.dev.white.adyax-dev.com/p/sanitaire/pack-wc-suspendu-daily-o2-sans-bride-avec-abattant-slim-frein-A6262889")

# _plus_button_page =
driver.find_element(By.XPATH, "//div[@class='product-action-zone']//div[@class='btn btn-plus']").click()
# _minus_button_page =
driver.find_element(By.XPATH, "//div[@class='product-action-zone']//div[@class='btn btn-minus']").click()

# _footer_fb =
elem = driver.find_element(By.XPATH, "//a[@data-sgt-social-host='Facebook']")
# or
#"//div[@class='social social-contact-to-us']//ul[1]/li[1]"
#"//div[@class='social social-contact-to-us']//ul[2]/li[1]"
elem.location_once_scrolled_into_view
elem.click()
driver.back()

# _ajouterAuPanier_button =
driver.find_element(By.XPATH, "//div[@class='product-action-zone']//div[@class='btn btn-regular']").click()
time.sleep(2)



# _plus_button_popin =
driver.find_element(By.XPATH, "//div[@class='product-recap product-change-qty sg-instance-calculation-widget-wrapper']//div[@class='btn btn-plus']").click()
driver.find_element(By.XPATH, "//div[@class='product-recap product-change-qty sg-instance-calculation-widget-wrapper']//div[@class='btn btn-plus']").click()
driver.find_element(By.XPATH, "//div[@class='product-recap product-change-qty sg-instance-calculation-widget-wrapper']//div[@class='btn btn-plus']").click()

# _minus_button_popin =
driver.find_element(By.XPATH, "//div[@class='product-recap product-change-qty sg-instance-calculation-widget-wrapper']//div[@class='btn btn-minus']").click()

# _qty_field_popin =
element = driver.find_element(By.XPATH, "//div[@class='product-recap product-change-qty sg-instance-calculation-widget-wrapper']//input[@type='text']")
ActionChains(driver).double_click(element).perform()
element.send_keys("567")

# _cross_button_popin =
driver.find_element(By.XPATH, "//div[@id='modal-add-to-cart']//a[@class='close-btn close']").click()

# _modifierLaQuantité_button_popin =
driver.find_element(By.LINK_TEXT, "Modifier la quantité").click()

# _poursuivreMesAchats_button_popin =
driver.find_element(By.LINK_TEXT, "Poursuivre mes achats").click()

# _voirmonpanier_button_popin =
driver.find_element(By.LINK_TEXT, "Voir mon panier").click()



