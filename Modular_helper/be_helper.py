from selenium import webdriver


validate_be_element = driver.find_element_by_name("")


def validate_be():
    validate_be_element.click()
    url  = validate_be_element.get_attribute("href")
    if url == "http://ashfkjshf.com"
        return True