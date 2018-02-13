from general.home_app_page import HomeAppPage
from general.base_test import BaseTest
from general.item_app_page import ItemAppPage
from general.create_new_account_app import CreateNewAccount
from general.home_app_page_logged_user import HomeAppPageLoggedUser
from selenium.webdriver.common.keys import Keys
import unicodedata

import pytest


class TestMainApp(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver, variables):
        self.vars = variables
        self.home_app_page=HomeAppPage(driver)
        self.item_app_page=ItemAppPage(driver)
        self.create_new_account_page=CreateNewAccount(driver)
        self.home_app_page_logged_user=HomeAppPageLoggedUser(driver)


    def not_test_count_number_of_stickers(self, driver):
# sel-5  - task 8 - http://software-testing.ru/lms/mod/assign/view.php?id=41866
        driver.get(self.vars["main_app_url"])
        driver.implicitly_wait(10)
        print ('Number of stickers on the main page {0}'.format(len(self.home_app_page.sticker())))


    def not_test_compare_data(self, driver):
# sel-5 - task 10 - http://software-testing.ru/lms/mod/assign/view.php?id=41869
# compare data on main page - campaign section and item page for every item

        driver.get(self.vars["main_app_url"])
        driver.implicitly_wait(10)
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
        driver.get(self.vars["main_app_url"])
        driver.implicitly_wait(10)
        self.home_app_page.creat_new_customer().click()
        email = self.create_new_account_page.create_new_account()
        driver.implicitly_wait(5)
        self.home_app_page_logged_user.logout().click()
        driver.implicitly_wait(5)
        self.home_app_page.email_field().send_keys(email)
        self.home_app_page.password_field().send_keys('Welcome1')
        driver.implicitly_wait(5)
        self.home_app_page.login_button().click()




        