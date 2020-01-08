login_field = driver.find_element_by_id("edit-login")
login_field.send_keys("belkacimi.smail@yopmail.com")

password_field = driver.find_element_by_id("edit-password")
password_field.send_keys("password")
password_field.send_keys(Keys.RETURN)

submit_button = driver.find_element_by_id("edit-submit").click()
submit_button.click()