from selenium import webdriver

driver = webdriver.Chrome()
with open("keywordfile.txt","r") as keywordfile:
    for values in keywordfile: #Reading row by row
        for keyword_elements in values.split(","): #Reading all columns in one TC

            if keyword_elements == "OpenBrowser":
                driver = webdriver.Chrome()
        #
            if "URL" in keyword_elements:
                driver.get(keyword_elements.split("-")[1])
        #
            if "close"  in keyword_elements:
                driver.close()
