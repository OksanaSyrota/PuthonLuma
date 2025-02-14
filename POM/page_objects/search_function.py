from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located, text_to_be_present_in_element
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'SearchField': (By.CSS_SELECTOR, '#search'),
    'ConfirmSearchIcon': (By.XPATH, '//*[@class="action search"]'),

}

class SearchFunction(BaseObject):


    #Search for an existing product/item and verify correct results are displayed.
    def click_empty_cart_icon(self):
        self.driver.find_element(*locators['CartIcon']).click()
        self.wait.until(element_to_be_clickable(locators['CloseIconMinicart']))