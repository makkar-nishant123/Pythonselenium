from selenium import webdriver
import unittest
import nose
from ddt import ddt, data, unpack
import xlrd

def getData(fileName):
    myrows = []
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    for row_index in range(1, sheet.nrows):
        myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return myrows

@ddt
class SearchResultDDT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @data(*getData("TestData.xlsx"))
    @unpack
    def test_SearchResults(self, search_values, expected_value):
        self.driver.get("http://demo.magentocommerce.com/")
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys(search_values)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        if expected_value > 0:
            self.assertEqual(expected_value, len(products))
        else:
            msg = self.driver.find_element_by_class_name("note-msg")
            self.assertEqual("Your search returns no results.", msg.text)

@classmethod
def tearDownClass(cls):
    cls.driver.quit()

if __name__=="__main__":
    nose.main()