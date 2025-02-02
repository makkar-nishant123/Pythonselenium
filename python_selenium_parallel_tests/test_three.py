import unittest
from time import sleep
from selenium import webdriver


class TestThree(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:9898/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
            })
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()

    def test_three(self):
        driver = self.driver
        driver.get("https://www.twitter.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()