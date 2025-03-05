import unittest

from POM.page_objects.product_detail_page import ProductDetailPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailPageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.product_detail_page = ProductDetailPage(cls.driver, cls.wait)
        cls.item_title = 'Argus All-Weather Tank'
        cls.driver.get('https://magento.softwaretestingboard.com/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))
        cls.driver.find_element(By.CSS_SELECTOR, '#search').send_keys(cls.item_title)
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Search"]')))
        cls.driver.find_element(By.CSS_SELECTOR, '[title="Search"]').click()
        cls.wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="product-item-link"])[1]')))
        cls.driver.find_element(By.XPATH, '(//*[@class="product-item-link"])[1]').click()
        cls.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.base')))


    def test_00_validate_main_option(self):
        self.assertEqual(self.item_title, self.product_detail_page.get_title_item())
        self.product_detail_page.get_price_item()
        self.product_detail_page.in_stock_option()
        self.product_detail_page.image_is_present()
        self.product_detail_page.click_add_to_wishlist()
        self.assertEqual('Customer Login', self.product_detail_page.customer_login_text())
        self.driver.back()
        self.product_detail_page.click_add_to_compare_link()
        self.assertEqual(f'You added product {self.item_title} to the comparison list.',
                         self.product_detail_page.get_added_to_comparison_list_text())
        self.assertEqual('Compare Products', self.product_detail_page.click_comparison_list_link())
        self.driver.back()
        self.product_detail_page.click_be_the_first_to_review()
        self.assertEqual("You're reviewing:", self.product_detail_page.get_you_are_reviewing_text())
        self.assertEqual(self.item_title, self.product_detail_page.get_item_title_from_review())
        self.driver.back()

    def test_add_to_cart_without_size(self):
        self.product_detail_page.click_color_option()
        self.product_detail_page.click_add_to_cart_button()
        self.assertEqual('This is a required field.', self.product_detail_page.get_error_message_for_size())
        self.driver.refresh()

    def test_add_to_cart_without_color(self):
        self.product_detail_page.click_size_option()
        self.product_detail_page.click_add_to_cart_button()
        self.assertEqual('This is a required field.', self.product_detail_page.get_error_message_for_color())
        self.driver.refresh()

    def test_add_to_cart(self):
        self.product_detail_page.click_size_option()
        self.product_detail_page.click_color_option()
        self.product_detail_page.enter_qty(2)
        self.product_detail_page.click_add_to_cart_button()
        self.assertEqual(f'You added {self.item_title} to your shopping cart.',
                         self.product_detail_page.get_success_message_add_to_cart())
        self.driver.refresh()

    def test_reviews_tab(self):
        self.product_detail_page.click_reviews_tab()
        self.assertEqual("You're reviewing:", self.product_detail_page.get_you_are_reviewing_text())
        self.assertEqual(self.item_title, self.product_detail_page.get_item_title_from_review())
        self.product_detail_page.click_five_stars_icon()
        self.product_detail_page.enter_nickname()
        self.product_detail_page.enter_summary()
        self.product_detail_page.enter_review()
        self.product_detail_page.click_submit_review_button()
        self.assertEqual('You submitted your review for moderation.',
                         self.product_detail_page.get_you_submitted_review_text())
        self.driver.refresh()

    def test_review_errors(self):
        self.product_detail_page.click_reviews_tab()
        self.product_detail_page.click_submit_review_button()
        self.assertEqual('Please select one of each of the ratings above.',
                         self.product_detail_page.get_rating_error())
        self.assertEqual('This is a required field.', self.product_detail_page.get_nickname_error())
        self.assertEqual('This is a required field.', self.product_detail_page.get_summary_error())
        self.assertEqual('This is a required field.', self.product_detail_page.get_review_error())
        self.driver.refresh()




        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
