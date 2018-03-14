from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor

class ChechoutAppPage(DriverConstructor):

    def items_in_the_cart(self):
        return self.driver.find_elements(By.XPATH, ".//li[@class='shortcut']/a[@href='#']")


    def remove_button(self):
        return self.driver.find_element(By.NAME, 'remove_cart_item')

    def payment_due(self):
        return self.driver.find_element(By.XPATH, "//*[@id='order_confirmation-wrapper']//td[2]/strong")


    def back_link(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Back')

    def items_in_the_cart_table(self):
        return self.driver.find_elements(By.XPATH, ".//td[@class='item']")