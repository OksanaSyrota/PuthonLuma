from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located, text_to_be_present_in_element
from sockshandler import is_ip

from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'SearchField': (By.CSS_SELECTOR, '#search'),
    'ConfirmSearchIcon': (By.XPATH, '//*[@class="action search"]'),
    'SearchResultTitle': (By.CSS_SELECTOR, '.base'),
    #'ProductsListSearchResult': (By.XPATH, '//*[@class="products list items product-items"]/li')
    'ProductsListSearchResult': (By.CSS_SELECTOR, '.product-image-photo'),
    'NoResultText': (By.XPATH, '//*[@class="message notice"]'),
    'PartSearchResultsList': (By.XPATH, '//*[@class="block"]/dd/a'),

}

class SearchFunction(BaseObject):


    #Search for an existing product/item and verify correct results are displayed.
    def enter_text_in_search_field(self, text_search):
        self.driver.find_element(*locators['SearchField']).send_keys(text_search)

    def click_confirm_search_icon(self):
        self.wait.until(element_to_be_clickable(locators['ConfirmSearchIcon']))
        self.driver.find_element(*locators['ConfirmSearchIcon']).click()
        self.wait.until(visibility_of_element_located(locators['SearchResultTitle']))
        return self.driver.find_element(*locators['SearchResultTitle']).text

    def check_list_of_items(self, word1, word2):
        items = self.driver.find_elements(*locators['ProductsListSearchResult'])
        titles = [item.get_attribute('alt') for item in items]
        words_to_check = [word1, word2]
        is_present = any(word in title for title in titles for word in words_to_check)
        print(is_present)

    def the_first_item_title(self, expected_title):
        items = self.driver.find_elements(*locators['ProductsListSearchResult'])
        if items and items[0].get_attribute('alt') == expected_title:
            return items[0].get_attribute('alt')

    #search for a Non-Existing Item
    def get_no_search_result_text(self):
        self.wait.until(visibility_of_element_located(locators['NoResultText']))
        return self.driver.find_element(*locators['NoResultText']).text.split("\n")[0]

    #Partial search input
    def check_list_of_items_with_partial_input(self, partial_input):
        items = self.driver.find_elements(*locators['ProductsListSearchResult'])
        titles = [item.get_attribute('alt') for item in items]
        is_present = (word in title for title in titles for word in partial_input)
        print(is_present)

    def check_related_search_terms_list(self, partial_input):
        items = self.driver.find_elements(*locators['PartSearchResultsList'])
        titles = [item.get_attribute('href') for item in items]
        is_present = (word in title for title in titles for word in partial_input)
        print(is_present)

    def get_search_results(self, search_query):
        search_field = self.driver.find_element(*locators['SearchField'])
        search_field.clear()
        search_field.send_keys(search_query)
        self.wait.until(element_to_be_clickable(locators['ConfirmSearchIcon']))
        self.driver.find_element(*locators['ConfirmSearchIcon']).click()
        self.wait.until(visibility_of_element_located(locators['ProductsListSearchResult']))
        items = self.driver.find_elements(*locators['ProductsListSearchResult'])
        return [item.get_attribute('alt') for item in items]


