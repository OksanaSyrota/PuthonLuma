import unittest

from POM.page_objects.search_function import SearchFunction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchFunctionTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.search_function = SearchFunction(cls.driver, cls.wait)
        cls.driver.get('https://magento.softwaretestingboard.com/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))

    def test_open_empty_minicart(self):
        self.header_navigation.click_empty_cart_icon()
        self.assertEqual('You have no items in your shopping cart.',
                         self.header_navigation.get_empty_minicart_text())



        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
