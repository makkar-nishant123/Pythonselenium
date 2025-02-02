import unittest
from time import sleep
from selenium import webdriver


class TestOne(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:9898/wd/hub",
            desired_capabilities={
                "browserName": "firefox",

            })
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("https://www.yahoo.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()