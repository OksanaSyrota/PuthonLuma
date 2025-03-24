from selenium.webdriver.support.expected_conditions import (element_to_be_clickable, visibility_of_element_located,
                                                            presence_of_element_located)
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
    'CustomerLoginTitle': (By.CSS_SELECTOR, '.base'),
    'AddToCompareLink': (By.XPATH, '(//*[@class="action tocompare"])[1]'),
    'AddedItemToCompareListText': (By.XPATH, '(//*[@class="messages"])[1]/div/div'),
    'ComparisonListLink': (By.XPATH, '(//*[@class="messages"])[1]/div/div/a'),
    'CompareProductsTitle': (By.CSS_SELECTOR, '.base'),
    'DetailsTab': (By.CSS_SELECTOR, '#tab-label-description-title'),
    'MoreInformationTab': (By.CSS_SELECTOR, '#tab-label-additional'),
    'ReviewsTab': (By.CSS_SELECTOR, '#tab-label-reviews-title'),
    #Reviews Tab
    'ReviewItemTitleText': (By.XPATH, '//*[@class="legend review-legend"]/strong'),
    'YouAreReviewingText': (By.XPATH, '//*[@class="legend review-legend"]/span'),
    'ReviewStars': (By.CSS_SELECTOR, '.radio'),
    'Rating5': (By.CSS_SELECTOR, '#Rating_5'),
    'NicknameField': (By.CSS_SELECTOR, '#nickname_field'),
    'SummaryField': (By.CSS_SELECTOR, '#summary_field'),
    'ReviewField': (By.CSS_SELECTOR, '#review_field'),
    'SubmitReviewButton': (By.XPATH, '//*[@class="primary actions-primary"]'),
    'RatingErrorText': (By.CSS_SELECTOR, 'div[id="ratings[4]-error"]'),
    'NicknameErrorText': (By.CSS_SELECTOR, '#nickname_field-error'),
    'SummaryErrorText': (By.CSS_SELECTOR, '#summary_field-error'),
    'ReviewErrorText': (By.CSS_SELECTOR, '#review_field-error'),
    'YouSubmittedReviewText': (By.XPATH, '(//*[@class="messages"])[1]/div/div'),
    'ItemImage': (By.XPATH, '(//*[@class="fotorama__img"])[1]'),
    'SuccessMessageAddToCart': (By.XPATH, '//*[@class="message-success success message"]'),
    'ErrorMessageForSize': (By.XPATH, '//*[contains(@id, "super_attribute[143]-error")]'),
    'ErrorMessageForColor': (By.XPATH, '//*[contains(@id, "super_attribute[93]-error")]')
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
        self.wait.until(visibility_of_element_located(locators['ItemImage']))
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

    def click_add_to_wishlist(self):
        self.wait.until(element_to_be_clickable(locators['AddToWishlistLink']))
        self.driver.find_element(*locators['AddToWishlistLink']).click()

    def customer_login_text(self):
        self.wait.until(visibility_of_element_located(locators['CustomerLoginTitle']))
        return self.driver.find_element(*locators['CustomerLoginTitle']).text

    def click_add_to_compare_link(self):
        self.wait.until(element_to_be_clickable(locators['AddToCompareLink']))
        self.driver.find_element(*locators['AddToCompareLink']).click()

    def get_added_to_comparison_list_text(self):
        self.wait.until(visibility_of_element_located(locators['AddedItemToCompareListText']))
        return self.driver.find_element(*locators['AddedItemToCompareListText']).text

    def click_comparison_list_link(self):
        self.wait.until(element_to_be_clickable(locators['ComparisonListLink']))
        self.driver.find_element(*locators['ComparisonListLink']).click()
        self.wait.until(visibility_of_element_located(locators['CompareProductsTitle']))
        return self.driver.find_element(*locators['CompareProductsTitle']).text

    #Reviews tab
    def click_reviews_tab(self):
        self.wait.until(element_to_be_clickable(locators['ReviewsTab']))
        self.driver.find_element(*locators['ReviewsTab']).click()

    def get_you_are_reviewing_text(self):
        self.wait.until(visibility_of_element_located(locators['YouAreReviewingText']))
        return self.driver.find_element(*locators['YouAreReviewingText']).text

    def get_item_title_from_review(self):
        self.wait.until(visibility_of_element_located(locators['ReviewItemTitleText']))
        return self.driver.find_element(*locators['ReviewItemTitleText']).text

    def click_five_stars_icon(self):
        self.wait.until(element_to_be_clickable(locators['Rating5']))
        element = self.driver.find_element(*locators['Rating5'])
        self.driver.execute_script("arguments[0].click();", element)

    def enter_nickname(self):
        self.wait.until(element_to_be_clickable(locators['NicknameField']))
        self.driver.find_element(*locators['NicknameField']).send_keys('Test')

    def enter_summary(self):
        self.wait.until(element_to_be_clickable(locators['SummaryField']))
        self.driver.find_element(*locators['SummaryField']).send_keys('Test')

    def enter_review(self):
        self.wait.until(element_to_be_clickable(locators['ReviewField']))
        self.driver.find_element(*locators['ReviewField']).send_keys('Test test test')

    def click_submit_review_button(self):
        self.wait.until(element_to_be_clickable(locators['SubmitReviewButton']))
        self.driver.find_element(*locators['SubmitReviewButton']).click()

    def get_you_submitted_review_text(self):
        self.wait.until(visibility_of_element_located(locators['YouSubmittedReviewText']))
        return self.driver.find_element(*locators['YouSubmittedReviewText']).text

    def get_rating_error(self):
        self.wait.until(visibility_of_element_located(locators['RatingErrorText']))
        return self.driver.find_element(*locators['RatingErrorText']).text

    def get_nickname_error(self):
        self.wait.until(visibility_of_element_located(locators['NicknameErrorText']))
        return self.driver.find_element(*locators['NicknameErrorText']).text

    def get_summary_error(self):
        self.wait.until(visibility_of_element_located(locators['SummaryErrorText']))
        return self.driver.find_element(*locators['SummaryErrorText']).text

    def get_review_error(self):
        self.wait.until(visibility_of_element_located(locators['ReviewErrorText']))
        return self.driver.find_element(*locators['ReviewErrorText']).text

    def click_be_the_first_to_review(self):
        self.wait.until(element_to_be_clickable(locators['BeTheFirstToReviewTheProductLink']))
        self.driver.find_element(*locators['BeTheFirstToReviewTheProductLink']).click()



