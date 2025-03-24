from selenium.common import NoSuchElementException
from selenium.webdriver.support.expected_conditions import (element_to_be_clickable, visibility_of_element_located,
                                                            presence_of_element_located, staleness_of, url_changes)
from POM.page_objects.base_object import BaseObject, driver
from selenium.webdriver.common.by import By


locators = {
    'ItemTitleCart': (By.XPATH, '(//*[@class="product-item-name"])[2]/a'),
    'ItemSizeCart': (By.XPATH, '(//*[@class="item-options"])[3]/dd[1]'),
    'ItemColorCart': (By.XPATH, '(//*[@class="item-options"])[3]/dd[2]'),
    'ItemPriceCart': (By.XPATH, '(//*[@class="cart-price"])[1]/span'),
    'QTYCart': (By.CSS_SELECTOR, '#cart-582628-qty'),
    'SearchField': (By.CSS_SELECTOR, '#search'),
    'ConfirmSearchIcon': (By.CSS_SELECTOR, '[title="Search"]'),
    'SizeOption': (By.XPATH, '//*[@class="swatch-option text"]'),
    'SizeOptionSecondChoice': (By.XPATH, '(//*[@class="swatch-attribute-options clearfix"])[1]/div[2]'),
    'ColorOption': (By.XPATH, '//*[@class="swatch-option color"]'),
    'AddToCartButton': (By.XPATH, '//*[@class="action primary tocart"]'),
    'ShoppingCartLink': (By.XPATH, '(//*[@class="messages"])[1]/div/div/a'),
    'ItemLink': (By.XPATH, '(//*[@class="product-item-link"])[1]'),
    'ItemTitleText': (By.CSS_SELECTOR, '.base'),
    'ShoppingCartTitle': (By.CSS_SELECTOR, '.base'),
    'SizeOptionCart': (By.XPATH, '//*[@class="item-options"]/dd[1]'),
    'ColorOptionCart': (By.XPATH, '//*[@class="item-options"]/dd[2]'),
    'SelectedSize': (By.XPATH, '(//*[@class="swatch-attribute-selected-option"])[1]'),
    'SelectedColor': (By.XPATH, '(//*[@class="swatch-attribute-selected-option"])[2]'),
    'QtyField': (By.CSS_SELECTOR, '#qty'),
    'QtyTextCart': (By.XPATH, '//*[@class="input-text qty"]'),
    'QtyTextSecondItemCart': (By.XPATH, '(//*[@class="input-text qty"])[2]'),
    'SubtotalPrice': (By.XPATH, '(//*[@class="cart-price"])[2]/span'),
    'SubtotalPriceSecondItem': (By.XPATH, '(//*[@class="cart-price"])[4]/span'),
    'EditIconCart': (By.XPATH, '(//*[@class="action action-edit"])[1]'),
    'DeleteIconCart': (By.XPATH, '(//*[@class="action action-delete"])[2]'),
    'UpdateShoppingCartButton': (By.XPATH, '//*[@class="action update"]'),
    'Body_Of_Page': (By.TAG_NAME, 'body'),
    'UpdateCartMessage': (By.XPATH, '//*[@class="message-success success message"]'),
    'SecondItemTitleCart': (By.XPATH, '(//*[@class="cart item"])[2]/tr/td/div/strong'),
    #Summary box
    'SummaryTitle': (By.CSS_SELECTOR, '.summary'),
    'EstimateShippingAndTaxOption': (By.CSS_SELECTOR, '#block-shipping-heading'),
    'SubtotalAmount': (By.XPATH, '(//*[@class="amount"])[1]/span'),
    'TaxAmount': (By.XPATH, '//*[@class="totals-tax"]/td/span'),
    'OrderTotalAmount': (By.XPATH, '//*[@class="grand totals"]/td/strong'),
    'ProceedToCheckoutButton': (By.XPATH, '//*[@data-role="proceed-to-checkout"]'),
    'CheckOutWithMultipleAddresses': (By.XPATH, '//*[@class="action multicheckout"]'),


}

class ShoppingCartPage(BaseObject):

    def search_item(self, item_title):
        self.driver.find_element(*locators['SearchField']).clear()
        self.driver.find_element(*locators['SearchField']).send_keys(item_title)
        self.wait.until(element_to_be_clickable(locators['ConfirmSearchIcon']))
        self.driver.find_element(*locators['ConfirmSearchIcon']).click()
        self.wait.until(element_to_be_clickable(locators['ItemLink']))
        self.driver.find_element(*locators['ItemLink']).click()

    def get_item_title_text(self):
        self.wait.until(visibility_of_element_located(locators['ItemTitleText']))
        return self.driver.find_element(*locators['ItemTitleText']).text

    def click_size_option(self):
        self.wait.until(element_to_be_clickable(locators['SizeOption']))
        self.driver.find_element(*locators['SizeOption']).click()

    def click_size_option_second_choice(self):
        self.wait.until(element_to_be_clickable(locators['SizeOptionSecondChoice']))
        self.driver.find_element(*locators['SizeOptionSecondChoice']).click()

    def click_color_option(self):
        self.wait.until(element_to_be_clickable(locators['ColorOption']))
        self.driver.find_element(*locators['ColorOption']).click()

    def click_add_to_cart_button(self):
        self.wait.until(element_to_be_clickable(locators['AddToCartButton']))
        self.driver.find_element(*locators['AddToCartButton']).click()

    def click_shopping_cart_link(self):
        self.wait.until(element_to_be_clickable(locators['ShoppingCartLink']))
        self.driver.find_element(*locators['ShoppingCartLink']).click()

    def get_shopping_cart_text(self):
        self.wait.until(url_changes(driver.current_url))
        self.wait.until(visibility_of_element_located(locators['ShoppingCartTitle']))
        return self.driver.find_element(*locators['ShoppingCartTitle']).text

    def get_selected_size_text(self):
        self.wait.until(visibility_of_element_located(locators['SelectedSize']))
        return self.driver.find_element(*locators['SelectedSize']).text

    def get_size_text_cart(self):
        self.wait.until(visibility_of_element_located(locators['SizeOptionCart']))
        return self.driver.find_element(*locators['SizeOptionCart']).text

    def get_selected_color_text(self):
        self.wait.until(visibility_of_element_located(locators['SelectedColor']))
        return self.driver.find_element(*locators['SelectedColor']).text

    def get_color_text_cart(self):
        self.wait.until(visibility_of_element_located(locators['ColorOptionCart']))
        return self.driver.find_element(*locators['ColorOptionCart']).text

    def enter_qty(self, qty):
        self.wait.until(visibility_of_element_located(locators['QtyField']))
        self.driver.find_element(*locators['QtyField']).clear()
        self.driver.find_element(*locators['QtyField']).send_keys(qty)

    def get_qty_cart(self):
        self.wait.until(visibility_of_element_located(locators['QtyTextCart']))
        return self.driver.find_element(*locators['QtyTextCart']).get_attribute('value')

    def get_subtotal_price(self):
        self.wait.until(visibility_of_element_located(locators['SubtotalPrice']))
        return self.driver.find_element(*locators['SubtotalPrice']).text

    def get_subtotal_price_for_second_item(self):
        self.wait.until(visibility_of_element_located(locators['SubtotalPriceSecondItem']))
        return self.driver.find_element(*locators['SubtotalPriceSecondItem']).text

    def enter_qty_cart_page(self, qty):
        self.wait.until(element_to_be_clickable(locators['QtyTextSecondItemCart']))
        self.driver.find_element(*locators['QtyTextSecondItemCart']).clear()
        self.driver.find_element(*locators['QtyTextSecondItemCart']).send_keys(qty)

    def click_update_shopping_cart_button(self):
        self.wait.until(element_to_be_clickable(locators['UpdateShoppingCartButton']))
        self.driver.find_element(*locators['UpdateShoppingCartButton']).click()
        self.wait.until(staleness_of(self.driver.find_element(*locators['Body_Of_Page'])))

    def click_edit_icon_cart(self):
        self.wait.until(element_to_be_clickable(locators['EditIconCart']))
        self.driver.find_element(*locators['EditIconCart']).click()

    def get_update_item_message(self):
        self.wait.until(visibility_of_element_located(locators['UpdateCartMessage']))
        return self.driver.find_element(*locators['UpdateCartMessage']).text

    def click_delete_icon(self):
        self.wait.until(element_to_be_clickable(locators['DeleteIconCart']))
        self.driver.find_element(*locators['DeleteIconCart']).click()
        self.wait.until(element_to_be_clickable(locators['UpdateShoppingCartButton']))
        try:
            self.driver.find_element(*locators['SecondItemTitleCart'])
            return False
        except NoSuchElementException:
            return True





