from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import xlrd
'''
file = "C:\\Users\\mrahmad\\Desktop\\Test.xlsx"
df = pd.read_excel(file,sheet_name="Sheet1")'''

driver = webdriver.Chrome()
driver.get("http://www.google.com")
#driver.maximize_window()
driver.find_element_by_xpath("(//*[text()='Gmail'])[1]").click()
driver.find_element_by_xpath("(//*[@class='h-c-header__cta-li h-c-header__cta-li--primary'])[2]/a").click()
time.sleep(2)
title1=driver.title
print(title1)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
title2= driver.title
print(title2)
file_location = "Data.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print(sheet.cell_value(0,0))
print(sheet.cell_value(0,1))
f= sheet.cell_value(1,0)
l= sheet.cell_value(1,1)
print(f)

driver.find_element_by_xpath("//*[@id='firstName']").send_keys(f)
driver.find_element_by_xpath("//*[@id='lastName']").send_keys(l)
