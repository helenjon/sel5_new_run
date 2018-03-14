from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import random

class ItemAppPage(DriverConstructor):

    def item_name(self):
        return self.driver.find_element(By.XPATH, "//h1[@class='title']")

    def item_manufacturer(self):
# in case Manufacturer not defined
        try:
            return  self.driver.find_element(By.XPATH, "//div[@class='manufacturer']/a/img").get_attribute('title')
        except NoSuchElementException:
            item_manufacturer = ''
            return item_manufacturer


    def item_regular_price(self):
        return self.driver.find_element(By.XPATH, "//div[@class='information']//s[@class='regular-price']")

    def item_campaign_price(self):
         return self.driver.find_element(By.XPATH, "//div[@class='information']//strong[@class='campaign-price']")


    def item_add_to_cart_button(self):
        return self.driver.find_element(By.NAME, 'add_cart_product')

    def product_size_drop_down(self):
        return self.driver.find_element(By.NAME, "options[Size]")

    def list_of_availbale_product_size(self):
        return self.driver.find_elements(By.XPATH, "//select[@name='options[Size]']/option")

    def similar_products_list(self):
        return self.driver.find_element(By.XPATH, "//*[@id='box-similar-products']/div/ul/li[@class='product column shadow hover-light']/a[@class='link']")




#other
    def get_list_of_availbale_product_size(self):
        list_of_available_product_size_value=[]
        i=1
        list_of_availbale_product_size=self.list_of_availbale_product_size()
        for all in list_of_availbale_product_size[1:]:
            list_of_available_product_size_value.append(all.get_attribute('value'))
            print all.get_attribute('value')
        return list_of_available_product_size_value

    def select_product_size(self):
        select = Select(self.product_size_drop_down())
        list_of_availbale_product_size= self.get_list_of_availbale_product_size()
        selected_value=list_of_availbale_product_size[random.randrange(0, len(list_of_availbale_product_size))]
        select.select_by_value(selected_value)
        print selected_value


