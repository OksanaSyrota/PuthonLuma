import time
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located, presence_of_element_located
from selenium.webdriver.support.select import Select
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'TitleItem': (By.CSS_SELECTOR, '.base'),
    'ItemPrice': (By.XPATH, '(//*[@class="price"])[1]'),
    'InStockText': (By.CSS_SELECTOR, '[title="Availability"]'),
    'BeTheFirstToReviewTheProductLink': (By.CSS_SELECTOR, '.reviews-actions'),
    'SizeOptions': (By.XPATH, '//*[@class="swatch-option text"]'),
    'ColorOptions': (By.XPATH, '//*[@class="swatch-option color"]'),
    'QtyField': (By.CSS_SELECTOR, '#qty'),
    'AddToCartButton': (By.CSS_SELECTOR, '#product-addtocart-button'),
    'AddToWishlistLink': (By.XPATH, '(//*[@data-action="add-to-wishlist"])[1]'),
    'AddToCompareLink': (By.XPATH, '(//*[@class="action tocompare"])[1]'),
    'DetailsTab': (By.CSS_SELECTOR, '#tab-label-description-title'),
    'MoreInformationTab': (By.CSS_SELECTOR, '#tab-label-additional'),
    'ReviewsTab': (By.CSS_SELECTOR, '#tab-label-reviews-title'),
    #Reviews Tab
    'ReviewItemTitleText': (By.XPATH, '//*[@class="legend review-legend"]/strong'),
    'ReviewStars': (By.CSS_SELECTOR, '.radio'),
    'NicknameField': (By.CSS_SELECTOR, '#nickname_field'),
    'SummaryField': (By.CSS_SELECTOR, '#summary_field'),
    'ReviewField': (By.CSS_SELECTOR, '#review_field'),
    'SubmitReviewButton': (By.XPATH, '//*[@class="primary actions-primary"]'),
    'ItemImage': (By.XPATH, '(//*[@class="fotorama__img"])[1]'),
    'SuccessMessageAddToCart': (By.XPATH, '//*[@class="message-success success message"]'),
    'ErrorMessageForSize': (By.XPATH, '//*[contains(@id, "super_attribute[143]-error")]'),
    'ErrorMessageForColor': (By.XPATH, '//*[contains(@id, "super_attribute[93]-error")]'),


}

class ProductDetailPage(BaseObject):

    def get_title_item(self):
        self.wait.until(visibility_of_element_located(locators['TitleItem']))
        item_title = self.driver.find_element(*locators['TitleItem']).text
        assert item_title, 'Item title is missing'
        return item_title

    def get_price_item(self):
        self.wait.until(visibility_of_element_located(locators['ItemPrice']))
        item_price = self.driver.find_element(*locators['ItemPrice']).text
        assert item_price, 'Item price is missing'
        print('Item Price is:', item_price)

    def in_stock_option(self):
        try:
            in_stock = self.wait.until(presence_of_element_located(locators['InStockText']))
            if in_stock.is_displayed():
                print('In stock is present')
                self.wait.until(element_to_be_clickable(locators['AddToCartButton']))
                print('"Add to cart" button is clickable')
            else:
                print('Item is out of stock')
        except Exception as e:
            print("Error:", e)

    def image_is_present(self):
        item_image = self.driver.find_element(*locators['ItemImage'])
        assert item_image.get_attribute('src'), 'Item image is missing'
        print('Item image is displayed')

    def click_size_option(self):
        self.wait.until(element_to_be_clickable(locators['SizeOptions']))
        self.driver.find_elements(*locators['SizeOptions'])[0].click()

    def click_color_option(self):
        self.wait.until(element_to_be_clickable(locators['ColorOptions']))
        self.driver.find_elements(*locators['ColorOptions'])[0].click()

    def enter_qty(self, qty):
        self.wait.until(visibility_of_element_located(locators['QtyField']))
        self.driver.find_element(*locators['QtyField']).clear()
        self.driver.find_element(*locators['QtyField']).send_keys(qty)

    def click_add_to_cart_button(self):
        self.wait.until(element_to_be_clickable(locators['AddToCartButton']))
        self.driver.find_element(*locators['AddToCartButton']).click()

    def get_success_message_add_to_cart(self):
        self.wait.until(visibility_of_element_located(locators['SuccessMessageAddToCart']))
        return self.driver.find_element(*locators['SuccessMessageAddToCart']).text

    def get_error_message_for_size(self):
        self.wait.until(visibility_of_element_located(locators['ErrorMessageForSize']))
        return self.driver.find_element(*locators['ErrorMessageForSize']).text

    def get_error_message_for_color(self):
        self.wait.until(visibility_of_element_located(locators['ErrorMessageForColor']))
        return self.driver.find_element(*locators['ErrorMessageForColor']).text



