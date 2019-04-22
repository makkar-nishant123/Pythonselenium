from selenium import  webdriver



def open_url(url):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(5)
    self.base_url = url
    self.verificationErrors = []
    self.accept_next_alert = True


def login(login_username,login_password,data1,data2):
    login_username.send_keys(data1)
    login_password.send_keys(data1)

def performorder():
    peform_order_element2.click()
    peform_order_element1.send_keys()

def logout():
    logout_button.click()


def validate_gui():
    validate_ui_element.click()
    url = validate_be_element.get_attribute("href")
    if url == "http://ashfkjshf.com"
        return True

