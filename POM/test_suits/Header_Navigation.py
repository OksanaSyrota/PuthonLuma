import unittest

from POM.page_objects.header_navigation import HeaderNavigation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HeaderNavigationTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.header_navigation = HeaderNavigation(cls.driver, cls.wait)
        cls.driver.get('https://magento.softwaretestingboard.com/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.showcart')))

    def test_open_empty_minicart(self):
        self.header_navigation.click_empty_cart_icon()
        self.assertEqual('You have no items in your shopping cart.',
                         self.header_navigation.get_empty_minicart_text())

    def test_women_drop_down_list(self):
        self.assertEqual(['Tops', 'Bottoms'], self.header_navigation.women_drop_down_list())
        self.assertEqual(['Jackets', 'Hoodies & Sweatshirts', 'Tees', 'Bras & Tanks'],
                         self.header_navigation.women_tops_drop_down_list())
        self.assertEqual(['Pants', 'Shorts'], self.header_navigation.women_bottoms_drop_down_list())
        self.header_navigation.women_drop_down_list()
        self.assertEqual('Tops', self.header_navigation.tops_link())
        self.header_navigation.women_drop_down_list()
        self.assertEqual('Bottoms', self.header_navigation.bottoms_link())
        self.header_navigation.women_tops_open_drop_down_list()
        self.assertEqual('Jackets', self.header_navigation.jacket_link())
        self.header_navigation.women_tops_open_drop_down_list()
        self.assertEqual('Hoodies & Sweatshirts', self.header_navigation.hoodies_sweartshirts_link())
        self.header_navigation.women_tops_open_drop_down_list()
        self.assertEqual('Tees', self.header_navigation.tees_link())
        self.header_navigation.women_tops_open_drop_down_list()
        self.assertEqual('Bras & Tanks', self.header_navigation.bras_tanks_link())
        self.header_navigation.women_bottoms_open_drop_down_list()
        self.assertEqual('Pants', self.header_navigation.pants_link())
        self.header_navigation.women_bottoms_open_drop_down_list()
        self.assertEqual('Shorts', self.header_navigation.shorts_link())

    def test_men_drop_down_list(self):
        self.assertEqual(['Tops', 'Bottoms'], self.header_navigation.men_drop_down_list())
        self.assertEqual(['Jackets', 'Hoodies & Sweatshirts', 'Tees', 'Tanks'],
                         self.header_navigation.men_tops_drop_down_list())
        self.assertEqual(['Pants', 'Shorts'], self.header_navigation.men_bottoms_drop_down_list())
        self.header_navigation.men_drop_down_list()
        self.assertEqual('Tops', self.header_navigation.men_tops_link())
        self.header_navigation.men_drop_down_list()
        self.assertEqual('Bottoms', self.header_navigation.men_bottoms_link())
        self.header_navigation.men_tops_open_drop_down_list()
        self.assertEqual('Jackets', self.header_navigation.men_jacket_link())
        self.header_navigation.men_tops_open_drop_down_list()
        self.assertEqual('Hoodies & Sweatshirts', self.header_navigation.men_hoodies_sweartshirts_link())
        self.header_navigation.men_tops_open_drop_down_list()
        self.assertEqual('Tees', self.header_navigation.men_tees_link())
        self.header_navigation.men_tops_open_drop_down_list()
        self.assertEqual('Tanks', self.header_navigation.men_tanks_link())
        self.header_navigation.men_bottoms_open_drop_down_list()
        self.assertEqual('Pants', self.header_navigation.men_pants_link())
        self.header_navigation.men_bottoms_open_drop_down_list()
        self.assertEqual('Shorts', self.header_navigation.men_shorts_link())

    def test_gear_drop_down_list(self):
        self.assertEqual(['Bags', 'Fitness Equipment', 'Watches'], self.header_navigation.gear_drop_down_list())
        self.assertEqual('Bags', self.header_navigation.gear_bags_link())
        self.assertEqual('Fitness Equipment', self.header_navigation.gear_fitness_equipment_link())
        self.assertEqual('Watches', self.header_navigation.gear_watches_link())

    def test_training_drop_down_list(self):
        self.assertEqual(['Video Download'], self.header_navigation.training_drop_down_list())
        self.assertEqual('Video Download', self.header_navigation.training_video_download_link())

    def test_main_navigation_links(self):
        self.assertEqual("What's New", self.header_navigation.whats_new_link())
        self.assertEqual("Women", self.header_navigation.women_link())
        self.assertEqual("Men", self.header_navigation.men_link())
        self.assertEqual("Gear", self.header_navigation.gear_link())
        self.assertEqual("Training", self.header_navigation.training_link())
        self.assertEqual("Sale", self.header_navigation.sale_link())
        self.assertEqual('Create New Customer Account', self.header_navigation.create_an_account_link())
        self.assertEqual('Customer Login', self.header_navigation.sign_in_link())







        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
