from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tourradar.com/d/europe")
action = ActionChains(driver);


driver.implicitly_wait(15)

elem1 = driver.find_element_by_xpath(".//li[@class='dropdown fill'][1]")
if elem1.is_displayed() is True:
    action.move_to_element(elem1).perform()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, ".//*[@class='dropdown fill hover']")))

elem2 = driver.find_element_by_xpath("//*[text()='Italy']")
elem2.click()

if driver.find_element_by_xpath("//*[text()='Italy tours']").is_displayed() is True:
    print("Navigated to Italy page")


driver.find_element_by_xpath("//*[@data-pid='april-2019']").click()
if driver.find_element_by_xpath("//*[text()='Walking the Amalfi Coast']").is_displayed() is True:
    print("Filter of Apr 2019 applied")

driver.back()