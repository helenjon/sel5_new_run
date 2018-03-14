from general.home_app_page import HomeAppPage
from general.base_test import BaseTest
from general.item_app_page import ItemAppPage
from general.checkout_app_page import ChechoutAppPage
from general.create_new_account_app import CreateNewAccount
from general.home_app_page_logged_user import HomeAppPageLoggedUser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unicodedata
import time

import pytest


class TestMainApp(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver, variables):
        self.vars = variables
        self.home_app_page=HomeAppPage(driver)
        self.item_app_page=ItemAppPage(driver)
        self.create_new_account_page=CreateNewAccount(driver)
        self.home_app_page_logged_user=HomeAppPageLoggedUser(driver)
        self.checkout_app_page=ChechoutAppPage(driver)
        driver.get(self.vars["main_app_url"])
        driver.implicitly_wait(10)

    def not_test_count_number_of_stickers(self, driver):
# sel-5  - task 8 - http://software-testing.ru/lms/mod/assign/view.php?id=41866
       # driver.get(self.vars["main_app_url"])
       # driver.implicitly_wait(10)
        print ('Number of stickers on the main page {0}'.format(len(self.home_app_page.sticker())))


    def not_test_compare_data(self, driver):
# sel-5 - task 10 - http://software-testing.ru/lms/mod/assign/view.php?id=41869
# compare data on main page - campaign section and item page for every item

        #driver.get(self.vars["main_app_url"])
        #driver.implicitly_wait(10)
        dictionaries=[]
        campaign_list = self.home_app_page.campaign_list()
        campaign_list_names = self.home_app_page.campaign_list_names()
        campaign_list_manufacturers = self.home_app_page.campaign_list_manufacturers()
        campaign_list_regular_prices = self.home_app_page.campaign_list_regular_prices()
        campaign_list_campaign_prices = self.home_app_page.campaign_list_campaign_prices()

#creating list with dictionaries
        dictionaries=self.home_app_page.dictionaries_fill_in(dictionaries, campaign_list)

#adding campaing list item information to the dictionary
        dictionaries_campaign_list = self.home_app_page.filling_in_dictionary(dictionaries, campaign_list,
                        campaign_list_names, campaign_list_manufacturers, campaign_list_regular_prices,
                        campaign_list_campaign_prices)


#opening all campaign items in new tabs
        for i in range (len(campaign_list)):
            campaign_list[i].send_keys(Keys.CONTROL + Keys.RETURN)


#get item attrebutes on item page
        for i in range(len(campaign_list)):
            driver.switch_to.window(driver.window_handles[-1])

            item_name = self.item_app_page.item_name().get_attribute('textContent')
            item_manufacturer = self.item_app_page.item_manufacturer()
            item_regular_price = self.item_app_page.item_regular_price()
            item_campaign_price = self.item_app_page.item_campaign_price()
# ------------- get price attrebutes for comparation
            item_regular_price1 = item_regular_price.get_attribute('textContent')
            item_campaign_price1 = item_campaign_price.get_attribute('textContent')
            item_colour_regular_prices = item_regular_price.value_of_css_property('color')
            item_font_size_regular_prices = item_regular_price.value_of_css_property('font-size')
            item_font_weight_regular_prices = item_regular_price.value_of_css_property('font-weight')
            item_colour_campaign_price = item_campaign_price.value_of_css_property('color')
            item_font_size_campaign_price = item_campaign_price.value_of_css_property('font-size')
            item_font_weight_campaign_price = item_campaign_price.value_of_css_property('font-weight')
            driver.close()
#comparation campaign data and item data

            self.home_app_page.compare(item_name, dictionaries_campaign_list[i]['name'])
#if manufacturer not defined on home page >> campaign it's sgous as empty sumbol in unicode
            self.home_app_page.compare(item_manufacturer, unicodedata.normalize("NFKD", dictionaries[i]['manufacturer']))
            self.home_app_page.compare(item_regular_price1, dictionaries[i]['regular_prices'])
            self.home_app_page.compare(item_campaign_price1, dictionaries[i]['campaign_prices'])
#-----
            self.home_app_page.compare(item_colour_regular_prices, dictionaries[i]['colour_regular_prices'])
            self.home_app_page.compare(item_font_size_regular_prices, dictionaries[i]['font_size_regular_prices'])
            self.home_app_page.compare(item_font_weight_regular_prices, dictionaries[i]['font_weight_regular_prices'])
            self.home_app_page.compare(item_colour_campaign_price, dictionaries[i]['color_campaign_price'])
            self.home_app_page.compare(item_font_size_campaign_price, dictionaries[i]['font_size_campaign_price'])
            self.home_app_page.compare(item_font_weight_campaign_price, dictionaries[i]['font_weight_campaign_price'])



    def not_test_create_new_accout(self, driver):
        #driver.get(self.vars["main_app_url"])
        #driver.implicitly_wait(10)
        self.home_app_page.creat_new_customer().click()
        email = self.create_new_account_page.create_new_account()
        driver.implicitly_wait(5)
        self.home_app_page_logged_user.logout().click()
        driver.implicitly_wait(5)
        self.home_app_page.email_field().send_keys(email)
        self.home_app_page.password_field().send_keys('Welcome1')
        driver.implicitly_wait(5)
        self.home_app_page.login_button().click()


    def test_add_product_to_basket(self, driver):
#get number of items in the cart
        quantity= self.home_app_page.cart_quantity().get_attribute('textContent')
        print ('Cart quantity = {} ').format(quantity)
        wait = WebDriverWait(driver, 10)
        self.home_app_page.most_popular()[0].click()
#adding products to cart
        while int(quantity)<3:
            try:
                self.item_app_page.product_size_drop_down()
                self.item_app_page.select_product_size()
                self.item_app_page.item_add_to_cart_button().click()
            except NoSuchElementException:
                self.item_app_page.item_add_to_cart_button().click()
            quantityplass = int(quantity) + 1
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(quantityplass)))
            quantity = self.home_app_page.cart_quantity().get_attribute('textContent')
            print ('Cart quantity = {} ').format(quantity)
            self.item_app_page.similar_products_list().click()
#removing product from cart
        self.home_app_page.checkout_cart_link().click()
        items_in_the_cart_table= self.checkout_app_page.items_in_the_cart_table()

        while len(items_in_the_cart_table)> 0:
            print ('Cart priducts in the cart = {} ').format(len(items_in_the_cart_table))
            if len(items_in_the_cart_table)>1:
                self.checkout_app_page.items_in_the_cart()[0].click()
                self.checkout_app_page.remove_button().click()
            else:
                self.checkout_app_page.remove_button().click()
            WebDriverWait(driver, 4).until(driver.find.element(By.NAME, 'remove_cart_item').is_enabled())
            items_in_the_cart_table=self.checkout_app_page.items_in_the_cart_table()

        self.checkout_app_page.back_link().click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='quantity']")))
        assert int(self.home_app_page.cart_quantity().get_attribute('textContent')) == 0







