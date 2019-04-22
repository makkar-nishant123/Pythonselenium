from Modular_helper.be_helper import validate_be
from Modular_helper.ui_helper import *

login_username = driver.find_element_by_name("")
login_password = driver.find_element_by_name("")
peform_order_element1 = driver.find_element_by_name("")
peform_order_element2 = driver.find_element_by_name("")
logout_button = driver.find_element_by_name("")
validate_gui_element = driver.find_element_by_name("")
validate_be_element = driver.find_element_by_name("")


login(login_username,login_password)
cancelorder(cancel_order_element1,cancel_order_element2)
logout(logout_button)
validate_gui(validate_gui_element)
validate_be(validate_be_element)

