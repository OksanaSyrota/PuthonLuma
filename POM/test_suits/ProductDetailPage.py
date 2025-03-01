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



        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
