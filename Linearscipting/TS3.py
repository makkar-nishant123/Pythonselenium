from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
base_url = "https://www.payu.in
verificationErrors = []
accept_next_alert = True

login_username = driver.find_element_by_name("")
login_password = driver.find_element_by_name("")
peform_order_element1 = driver.find_element_by_name("")
peform_order_element2 = driver.find_element_by_name("")
logout_button = driver.find_element_by_name("")
validate_gui_element = driver.find_element_by_name("")
validate_be_element = driver.find_element_by_name("")


#Performing login
login_username.send_keys("username")
login_username.send_keys("password")

#Performing Order
peform_order_element2.click()
peform_order_element1.send_keys()


#Performing Logout
logout_button.click()



validate_be_element.click()
url = validate_be_element.get_attribute("href")
if url == "http://ashfkjshf.com"
    print (True)



validate_ui_element.click()
url = validate_be_element.get_attribute("href")
if url == "http://ashfkjshf.com"
    print(True)