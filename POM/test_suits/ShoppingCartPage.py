import unittest

from POM.page_objects.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.shopping_cart_page = ShoppingCartPage(cls.driver, cls.wait)
        cls.item_title = 'Argus All-Weather Tank'
        cls.driver.get('https://magento.softwaretestingboard.com/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))
        cls.driver.find_element(By.CSS_SELECTOR, '#search').send_keys(cls.item_title)
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Search"]')))
        cls.driver.find_element(By.CSS_SELECTOR, '[title="Search"]').click()
        cls.wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="product-item-link"])[1]')))
        cls.driver.find_element(By.XPATH, '(//*[@class="product-item-link"])[1]').click()
        cls.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="swatch-option text"]')))
        cls.driver.find_element(By.XPATH, '//*[@class="swatch-option text"]').click()
        cls.driver.find_element(By.XPATH, '//*[@class="swatch-option color"]').click()
        cls.driver.find_element(By.CSS_SELECTOR, '#product-addtocart-button').click()
        cls.wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="messages"])[1]/div/div/a')))
        cls.driver.find_element(By.XPATH, '(//*[@class="messages"])[1]/div/div/a').click()
        cls.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.base')))


    def test_shopping_cart(self):
        self.assertEqual('Shopping Cart', self.shopping_cart_page.get_shopping_cart_title())



        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
