import unittest

from POM.page_objects.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.shopping_cart_page = ShoppingCartPage(cls.driver, cls.wait)
        cls.driver.get('https://magento.softwaretestingboard.com/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))


    def test_first_item(self):
        self.shopping_cart_page.search_item('Radiant Tee')
        self.assertEqual('Radiant Tee', self.shopping_cart_page.get_item_title_text())
        self.shopping_cart_page.click_size_option()
        self.shopping_cart_page.click_color_option()
        size_option = self.shopping_cart_page.get_selected_size_text()
        color_option = self.shopping_cart_page.get_selected_color_text()
        self.shopping_cart_page.enter_qty(2)
        self.shopping_cart_page.click_add_to_cart_button()
        self.shopping_cart_page.click_shopping_cart_link()
        self.assertEqual('Shopping Cart', self.shopping_cart_page.get_shopping_cart_text())
        self.assertEqual(size_option, self.shopping_cart_page.get_size_text_cart())
        self.assertEqual(color_option, self.shopping_cart_page.get_color_text_cart())
        self.assertEqual('2', self.shopping_cart_page.get_qty_cart())
        self.assertEqual('$44.00', self.shopping_cart_page.get_subtotal_price())
        self.shopping_cart_page.click_edit_icon_cart()
        self.assertEqual('Radiant Tee', self.shopping_cart_page.get_item_title_text())
        self.shopping_cart_page.click_size_option_second_choice()
        size_option = self.shopping_cart_page.get_selected_size_text()
        self.shopping_cart_page.click_color_option()
        self.shopping_cart_page.click_add_to_cart_button()
        self.assertEqual('Radiant Tee was updated in your shopping cart.',
                         self.shopping_cart_page.get_update_item_message())
        self.assertEqual(size_option, self.shopping_cart_page.get_size_text_cart())

    def test_second_item(self):
        self.shopping_cart_page.search_item('Breathe-Easy Tank')
        self.assertEqual('Breathe-Easy Tank', self.shopping_cart_page.get_item_title_text())
        self.shopping_cart_page.click_size_option()
        self.shopping_cart_page.click_color_option()
        self.shopping_cart_page.click_add_to_cart_button()
        self.shopping_cart_page.click_shopping_cart_link()
        self.assertEqual('Shopping Cart', self.shopping_cart_page.get_shopping_cart_text())
        self.shopping_cart_page.enter_qty_cart_page(2)
        self.shopping_cart_page.click_update_shopping_cart_button()
        self.assertEqual('$68.00', self.shopping_cart_page.get_subtotal_price_for_second_item())
        self.shopping_cart_page.click_delete_icon()




        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
