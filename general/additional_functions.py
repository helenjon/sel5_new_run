from driver_constructor import DriverConstructor
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from general.home_app_page import HomeAppPage
from general.item_app_page import ItemAppPage
from general.checkout_app_page import ChechoutAppPage
from time import sleep
from general.create_new_account_app import CreateNewAccount
from general.home_app_page_logged_user import HomeAppPageLoggedUser
from selenium.webdriver.common.keys import Keys


class AdditionalFunctions(DriverConstructor):

    def add_item_to_cart(self):
        quantity = 0
        self.item_app_page=ItemAppPage(self.driver)
        self.home_app_page=HomeAppPage(self.driver)
        while int(quantity) < 3:
            try:
                self.item_app_page.product_size_drop_down()
                self.item_app_page.select_product_size()
                self.item_app_page.item_add_to_cart_button().click()
            except NoSuchElementException:
                self.item_app_page.item_add_to_cart_button().click()
            quantityplass = int(quantity) + 1
            WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(quantityplass)))
            quantity = self.home_app_page.cart_quantity().get_attribute('textContent')
            print ('Cart quantity = {} ').format(quantity)
            self.item_app_page.similar_products_list().click()

    def remove_item_from_cart(self):
        self.checkout_app_page = ChechoutAppPage(self.driver)
        items_in_the_cart_table = self.checkout_app_page.items_in_the_cart_table()
        while len(items_in_the_cart_table) > 0:
            print ('Cart priducts in the cart = {} ').format(len(items_in_the_cart_table))
            if len(items_in_the_cart_table) > 1:
                self.checkout_app_page.items_in_the_cart()[0].click()
                remove_old = self.checkout_app_page.remove_button()
                self.checkout_app_page.remove_button().click()
            else:
                remove_old = self.checkout_app_page.remove_button()
                self.checkout_app_page.remove_button().click()
            sleep(3)
            WebDriverWait(self.driver, 4).until(EC.staleness_of(remove_old))
            items_in_the_cart_table = self.checkout_app_page.items_in_the_cart_table()
            # go to home page to check all cart
            # added wait becouse Back button became available not imideately after removing action
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Back')))






