from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://hotline.ua")
# #driver.find_element_by_xpath('//*[@id="page"]/section[1]/div/div[3]/div[2]/div[2]/a').click()
element = driver.find_element(By.ID, "searchbox")
element.send_keys("iPhone")
time.sleep(2)
select = driver.find_element(By.XPATH, '//*[@id="live-search"]//li[4]//a')
select.click()
select = driver.find_element(By.XPATH, '//li[@data-id="prices"]')
select.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)
for i in driver.find_elements_by_xpath('//div[@data-selector="price-line"]'):
    print(driver.find_element_by_xpath('//a[@data-tracking-id="offer-1"]').text)
    print(driver.find_element_by_xpath('//div[@class="cell-2 cell-md m_b-sm"]').text)
    print(driver.find_element_by_xpath('//span[@class="price-format"]').text)


#time.sleep(2)
#for i in driver.find_elements_by_xpath('//a[@data-tracking-id="offer-1"]'):
#    print(i.text)

#time.sleep(2)
#for i in driver.find_elements_by_xpath('//div[@class="cell-2 cell-md m_b-sm"]'):
#    print(i.text)

#time.sleep(2)
#for i in driver.find_elements_by_xpath('//span[@class="price-format"]'):
#    print(i.text)







#element = driver.find_element(By.XPATH, "//*[@id='item-product-1']/div/div/ul/li[9]/a")

#element.click()
#driver.find_element(By.XPATH, "//div[2][@class='btn']").click()
#time.sleep(2)
