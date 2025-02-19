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

    def test_search_valid_item_title(self):
        self.search_function.enter_text_in_search_field('Layla Tee')
        self.assertEqual("Search results for: 'Layla Tee'", self.search_function.click_confirm_search_icon())
        #check if search list of items have at least one word from entered text
        self.search_function.check_list_of_items('Layla', 'Tee')
        #check if the first item is the item from entered text in the search field
        self.assertEqual('Layla Tee', self.search_function.the_first_item_title('Layla Tee'))

    #Search for a Non-Existing Item
    def test_search_for_a_Non_Existing_Item(self):
        self.search_function.enter_text_in_search_field('Test')
        self.assertEqual("Search results for: 'Test'", self.search_function.click_confirm_search_icon())
        self.assertEqual("Your search returned no results.", self.search_function.get_no_search_result_text())

    #Partial Search Input
    def test_partial_search_input(self):
        self.search_function.enter_text_in_search_field('Sho')
        self.assertEqual("Search results for: 'Sho'", self.search_function.click_confirm_search_icon())
        #check if search list of items have partial input
        self.search_function.check_list_of_items_with_partial_input('Sho')
        #check if related search terms have partial input
        self.search_function.check_related_search_terms_list('Sho')

    #Case Insensitivity (Search with different cases ("t shirt" vs. "t-shirt") and verify that results remain the same)
    def test_case_insensitivity(self):
        result1 = self.search_function.get_search_results('t shirt')
        result2 = self.search_function.get_search_results('t-shirt')
        if result1 == result2:
            print("Both searches returned the same list of items.")







        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
