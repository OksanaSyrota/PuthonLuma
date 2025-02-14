from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located, text_to_be_present_in_element
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'CartIcon': (By.CSS_SELECTOR, '.showcart'),
    'EmptyMinicartMessage': (By.CSS_SELECTOR, '.subtitle'),
    'ProceedToCheckoutButtonMinicart': (By.CSS_SELECTOR, '#top-cart-btn-checkout'),
    'CloseIconMinicart': (By.CSS_SELECTOR, '#btn-minicart-close'),
    'SignInLink': (By.XPATH, '(//*[@class="header links"]//a)[2]'),
    'CustomerLoginTitle': (By.CSS_SELECTOR, '.base'),
    'CreateAnAccountLink': (By.XPATH, '(//*[@class="header links"]//a)[3]'),
    'CreateNewCustomerAccountTitle': (By.CSS_SELECTOR, '.base'),
    'SearchField': (By.CSS_SELECTOR, '#search'),
    'LumaLogo': (By.CSS_SELECTOR, '.logo'),
    'WhatsNewLink': (By.CSS_SELECTOR, '#ui-id-3'),
    'WhatsNewTitle': (By.CSS_SELECTOR, '.base'),
    'WomenLink': (By.CSS_SELECTOR, '#ui-id-4'),
    'WomenTitle': (By.CSS_SELECTOR, '.base'),
    #'Women' drop-down list
    'WomenDropDownList': (By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul/li'),
    'TopsDropDownList': (By.XPATH, '(//*[@id="ui-id-2"]/li[2]/ul/li/ul)[1]/li'),
    'BottomsDropDownList': (By.XPATH, '(//*[@id="ui-id-2"]/li[2]/ul/li/ul)[2]/li'),
    'TopsLink': (By.CSS_SELECTOR, '#ui-id-9'),
    'TopsTitle': (By.CSS_SELECTOR, '.base'),
    'JacketLink': (By.CSS_SELECTOR, '#ui-id-11'),
    'JacketTitle': (By.CSS_SELECTOR, '.base'),
    'Hoodies&SweatshirtLink': (By.CSS_SELECTOR, '#ui-id-12'),
    'Hoodies&SweatshirtTitle': (By.CSS_SELECTOR, '.base'),
    'TeesLink': (By.CSS_SELECTOR, '#ui-id-13'),
    'TeesTitle': (By.CSS_SELECTOR, '.base'),
    'Bras&TanksLink': (By.CSS_SELECTOR, '#ui-id-14'),
    'Bras&TanksTitle': (By.CSS_SELECTOR, '.base'),
    'BottomsLink': (By.CSS_SELECTOR, '#ui-id-10'),
    'BottomsTitle': (By.CSS_SELECTOR, '.base'),
    'PantsLink': (By.CSS_SELECTOR, '#ui-id-15'),
    'PantsTitle': (By.CSS_SELECTOR, '.base'),
    'ShortsLink': (By.CSS_SELECTOR, '#ui-id-16'),
    'ShortsTitle': (By.CSS_SELECTOR, '.base'),
    #'Men' drop-down list
    'MenDropDownList': (By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li'),
    'MenTopsDropDownList': (By.XPATH, '(//*[@id="ui-id-2"]/li[3]/ul/li/ul)[1]/li'),
    'MenBottomsDropDownList': (By.XPATH, '(//*[@id="ui-id-2"]/li[3]/ul/li/ul)[2]/li'),
    'MenTopsLink': (By.CSS_SELECTOR, '#ui-id-17'),
    'MenTopsTitle': (By.CSS_SELECTOR, '.base'),
    'MenJacketLink': (By.CSS_SELECTOR, '#ui-id-19'),
    'MenJacketTitle': (By.CSS_SELECTOR, '.base'),
    'MenHoodies&SweatshirtLink': (By.CSS_SELECTOR, '#ui-id-20'),
    'MenHoodies&SweatshirtTitle': (By.CSS_SELECTOR, '.base'),
    'MenTeesLink': (By.CSS_SELECTOR, '#ui-id-21'),
    'MenTeesTitle': (By.CSS_SELECTOR, '.base'),
    'MenTanksLink': (By.CSS_SELECTOR, '#ui-id-22'),
    'MenTanksTitle': (By.CSS_SELECTOR, '.base'),
    'MenBottomsLink': (By.CSS_SELECTOR, '#ui-id-18'),
    'MenBottomsTitle': (By.CSS_SELECTOR, '.base'),
    'MenPantsLink': (By.CSS_SELECTOR, '#ui-id-23'),
    'MenPantsTitle': (By.CSS_SELECTOR, '.base'),
    'MenShortsLink': (By.CSS_SELECTOR, '#ui-id-24'),
    'MenShortsTitle': (By.CSS_SELECTOR, '.base'),
    'MenLink': (By.CSS_SELECTOR, '#ui-id-5'),
    'MenTitle': (By.CSS_SELECTOR, '.base'),
    #'Gear' drop-down list
    'GearLink': (By.CSS_SELECTOR, '#ui-id-6'),
    'GearTitle': (By.CSS_SELECTOR, '.base'),
    'GearDropDownList': (By.XPATH, '//*[@id="ui-id-2"]/li[4]/ul/li'),
    'BagsLink': (By.CSS_SELECTOR, '#ui-id-25'),
    'BagsTitle': (By.CSS_SELECTOR, '.base'),
    'FitnessEquipmentLink': (By.CSS_SELECTOR, '#ui-id-26'),
    'FitnessEquipmentTitle': (By.CSS_SELECTOR, '.base'),
    'WatchesLink': (By.CSS_SELECTOR, '#ui-id-27'),
    'WatchesTitle': (By.CSS_SELECTOR, '.base'),
    #'Training' drop-down list
    'TrainingLink': (By.CSS_SELECTOR, '#ui-id-7'),
    'TrainingTitle': (By.CSS_SELECTOR, '.base'),
    'TrainingDropDownList': (By.XPATH, '//*[@id="ui-id-2"]/li[5]/ul/li'),
    'VideoDownloadLink': (By.CSS_SELECTOR, '#ui-id-28'),
    'VideoDownloadTitle': (By.CSS_SELECTOR, '.base'),
    'SaleLink': (By.CSS_SELECTOR, '#ui-id-8'),
    'SaleTitle': (By.CSS_SELECTOR, '.base'),

}


class HeaderNavigation(BaseObject):


    def click_empty_cart_icon(self):
        self.driver.find_element(*locators['CartIcon']).click()
        self.wait.until(element_to_be_clickable(locators['CloseIconMinicart']))

    def get_empty_minicart_text(self):
        return self.driver.find_element(*locators['EmptyMinicartMessage']).text

    def sign_in_link(self):
        self.driver.find_element(*locators['SignInLink']).click()
        self.wait.until(visibility_of_element_located(locators['CustomerLoginTitle']))
        return self.driver.find_element(*locators['CustomerLoginTitle']).text

    def create_an_account_link(self):
        self.driver.find_element(*locators['CreateAnAccountLink']).click()
        self.wait.until(visibility_of_element_located(locators['CreateNewCustomerAccountTitle']))
        return self.driver.find_element(*locators['CreateNewCustomerAccountTitle']).text

    def whats_new_link(self):
        self.driver.find_element(*locators['WhatsNewLink']).click()
        self.wait.until(visibility_of_element_located(locators['WhatsNewTitle']))
        return self.driver.find_element(*locators['WhatsNewTitle']).text

    def women_link(self):
        self.driver.find_element(*locators['WomenLink']).click()
        self.wait.until(visibility_of_element_located(locators['WomenTitle']))
        return self.driver.find_element(*locators['WomenTitle']).text

    def men_link(self):
        self.driver.find_element(*locators['MenLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenTitle']))
        return self.driver.find_element(*locators['MenTitle']).text

    def gear_link(self):
        self.driver.find_element(*locators['GearLink']).click()
        self.wait.until(visibility_of_element_located(locators['GearTitle']))
        return self.driver.find_element(*locators['GearTitle']).text

    def training_link(self):
        self.driver.find_element(*locators['TrainingLink']).click()
        self.wait.until(visibility_of_element_located(locators['TrainingTitle']))
        return self.driver.find_element(*locators['TrainingTitle']).text

    def sale_link(self):
        self.driver.find_element(*locators['SaleLink']).click()
        self.wait.until(visibility_of_element_located(locators['SaleTitle']))
        return self.driver.find_element(*locators['SaleTitle']).text

    def women_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['TopsLink']))
        drop_down_links = self.driver.find_elements(*locators['WomenDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def women_tops_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['TopsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['TopsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['JacketLink']))
        drop_down_links = self.driver.find_elements(*locators['TopsDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def women_bottoms_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['BottomsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['BottomsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['PantsLink']))
        drop_down_links = self.driver.find_elements(*locators['BottomsDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def women_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['BottomsLink']))

    def women_tops_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['TopsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['TopsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['JacketLink']))

    def women_bottoms_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['WomenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['BottomsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['BottomsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['PantsLink']))

    def tops_link(self):
        self.driver.find_element(*locators['TopsLink']).click()
        self.wait.until(visibility_of_element_located(locators['TopsTitle']))
        return self.driver.find_element(*locators['TopsTitle']).text

    def jacket_link(self):
        self.driver.find_element(*locators['JacketLink']).click()
        self.wait.until(visibility_of_element_located(locators['JacketTitle']))
        return self.driver.find_element(*locators['JacketTitle']).text

    def hoodies_sweartshirts_link(self):
        self.driver.find_element(*locators['Hoodies&SweatshirtLink']).click()
        self.wait.until(visibility_of_element_located(locators['Hoodies&SweatshirtTitle']))
        return self.driver.find_element(*locators['Hoodies&SweatshirtTitle']).text

    def tees_link(self):
        self.driver.find_element(*locators['TeesLink']).click()
        self.wait.until(visibility_of_element_located(locators['TeesTitle']))
        return self.driver.find_element(*locators['TeesTitle']).text

    def bras_tanks_link(self):
        self.driver.find_element(*locators['Bras&TanksLink']).click()
        self.wait.until(visibility_of_element_located(locators['Bras&TanksTitle']))
        return self.driver.find_element(*locators['Bras&TanksTitle']).text

    def bottoms_link(self):
        self.driver.find_element(*locators['BottomsLink']).click()
        self.wait.until(visibility_of_element_located(locators['BottomsTitle']))
        return self.driver.find_element(*locators['BottomsTitle']).text

    def pants_link(self):
        self.driver.find_element(*locators['PantsLink']).click()
        self.wait.until(visibility_of_element_located(locators['PantsTitle']))
        return self.driver.find_element(*locators['PantsTitle']).text

    def shorts_link(self):
        self.driver.find_element(*locators['ShortsLink']).click()
        self.wait.until(visibility_of_element_located(locators['ShortsTitle']))
        return self.driver.find_element(*locators['ShortsTitle']).text

#Men drop-down
    def men_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenTopsLink']))
        drop_down_links = self.driver.find_elements(*locators['MenDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def men_tops_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenTopsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenTopsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenJacketLink']))
        drop_down_links = self.driver.find_elements(*locators['MenTopsDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def men_bottoms_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenBottomsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenBottomsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenPantsLink']))
        drop_down_links = self.driver.find_elements(*locators['MenBottomsDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def men_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenBottomsLink']))

    def men_tops_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenTopsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenTopsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenJacketLink']))

    def men_bottoms_open_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenBottomsLink']))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['MenBottomsLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['MenPantsLink']))

    def men_tops_link(self):
        self.driver.find_element(*locators['MenTopsLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenTopsTitle']))
        return self.driver.find_element(*locators['MenTopsTitle']).text

    def men_jacket_link(self):
        self.driver.find_element(*locators['MenJacketLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenJacketTitle']))
        return self.driver.find_element(*locators['MenJacketTitle']).text

    def men_hoodies_sweartshirts_link(self):
        self.driver.find_element(*locators['MenHoodies&SweatshirtLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenHoodies&SweatshirtTitle']))
        return self.driver.find_element(*locators['MenHoodies&SweatshirtTitle']).text

    def men_tees_link(self):
        self.driver.find_element(*locators['MenTeesLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenTeesTitle']))
        return self.driver.find_element(*locators['MenTeesTitle']).text

    def men_tanks_link(self):
        self.driver.find_element(*locators['MenTanksLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenTanksTitle']))
        return self.driver.find_element(*locators['MenTanksTitle']).text

    def men_bottoms_link(self):
        self.driver.find_element(*locators['MenBottomsLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenBottomsTitle']))
        return self.driver.find_element(*locators['MenBottomsTitle']).text

    def men_pants_link(self):
        self.driver.find_element(*locators['MenPantsLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenPantsTitle']))
        return self.driver.find_element(*locators['MenPantsTitle']).text

    def men_shorts_link(self):
        self.driver.find_element(*locators['MenShortsLink']).click()
        self.wait.until(visibility_of_element_located(locators['MenShortsTitle']))
        return self.driver.find_element(*locators['MenShortsTitle']).text

    #Gear drop-down
    def gear_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['GearLink'])).perform()
        self.wait.until(visibility_of_element_located(locators['BagsLink']))
        drop_down_links = self.driver.find_elements(*locators['GearDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def gear_bags_link(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['GearLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['BagsLink']))
        self.driver.find_element(*locators['BagsLink']).click()
        self.wait.until(visibility_of_element_located(locators['BagsTitle']))
        return self.driver.find_element(*locators['BagsTitle']).text

    def gear_fitness_equipment_link(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['GearLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['FitnessEquipmentLink']))
        self.driver.find_element(*locators['FitnessEquipmentLink']).click()
        self.wait.until(visibility_of_element_located(locators['FitnessEquipmentTitle']))
        return self.driver.find_element(*locators['FitnessEquipmentTitle']).text

    def gear_watches_link(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['GearLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['WatchesLink']))
        self.driver.find_element(*locators['WatchesLink']).click()
        self.wait.until(visibility_of_element_located(locators['WatchesTitle']))
        return self.driver.find_element(*locators['WatchesTitle']).text

    #Training drop-down
    def training_drop_down_list(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['TrainingLink'])).perform()
        self.wait.until(visibility_of_element_located(locators['VideoDownloadLink']))
        drop_down_links = self.driver.find_elements(*locators['TrainingDropDownList'])
        titles = [link.text for link in drop_down_links]
        return titles

    def training_video_download_link(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locators['TrainingLink'])).perform()
        self.wait.until(element_to_be_clickable(locators['VideoDownloadLink']))
        self.driver.find_element(*locators['VideoDownloadLink']).click()
        self.wait.until(visibility_of_element_located(locators['VideoDownloadTitle']))
        return self.driver.find_element(*locators['VideoDownloadTitle']).text


