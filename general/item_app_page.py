from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from selenium.common.exceptions import NoSuchElementException

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


