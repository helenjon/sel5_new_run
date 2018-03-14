from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor




class HomeAppPage(DriverConstructor):

    def most_popular(self):
        return self.driver.find_elements(By.XPATH, '//*[@id="box-most-popular"]/div/ul/li/a[1]')

    def cart_quantity(self):
        return self.driver.find_element(By.XPATH, "//span[@class='quantity']")

    def sticker(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'div.sticker')


    def campaign_list (self):
        return self.driver.find_elements(By.XPATH, "//*[@id='box-campaigns']/div//a[@class='link']")

    def campaign_list_names(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//div[@class='name']")


    def campaign_list_manufacturers(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//div[@class='manufacturer']")


    def campaign_list_regular_prices(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//s[@class='regular-price']")


    def campaign_list_campaign_prices(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//strong[@class='campaign-price']")


    def creat_new_customer(self):
        return self.driver.find_element_by_partial_link_text('New customers click here')

    def login_button(self):
        return self.driver.find_element(By.NAME, 'login')

    def email_field(self):
        return self.driver.find_element(By.NAME, 'email')

    def password_field(self):
        return self.driver.find_element(By.NAME, 'password')

    def checkout_cart_link(self):
        return self.driver.find_element(By.XPATH, "//*[@id='cart']/a[3]")

#other

    def dictionaries_fill_in(self, dictionaries, campaign_list):
        for i in range (len(campaign_list)):
             dictionaries.append('dictionary_name')
        return dictionaries

    def filling_in_dictionary(self, dictionaries, campaign_list, campaign_list_names,
                              campaign_list_manufacturers, campaign_list_regular_prices, campaign_list_campaign_prices ):
        for i in range (len(campaign_list)):
            dictionaries[i]={}
            dictionaries[i]['name'] = campaign_list_names[i].get_attribute('textContent')
            dictionaries[i]['manufacturer'] = campaign_list_manufacturers[i].get_attribute('textContent')
            dictionaries[i]['regular_prices'] = campaign_list_regular_prices[i].get_attribute('textContent')
            dictionaries[i]['campaign_prices'] = campaign_list_campaign_prices[i].get_attribute('textContent')
 # --------------------------
            dictionaries[i]['colour_regular_prices'] = campaign_list_regular_prices[i].value_of_css_property('color')
            dictionaries[i]['font_size_regular_prices'] = campaign_list_regular_prices[i].value_of_css_property('font-size')
            dictionaries[i]['font_weight_regular_prices'] = campaign_list_regular_prices[i].value_of_css_property('font-weight')
            dictionaries[i]['color_campaign_price'] = campaign_list_campaign_prices[i].value_of_css_property('color')
            dictionaries[i]['font_size_campaign_price'] = campaign_list_campaign_prices[i].value_of_css_property('font-size')
            dictionaries[i]['font_weight_campaign_price'] = campaign_list_campaign_prices[i].value_of_css_property('font-weight')
        return dictionaries


    def compare(self, item_data, compain_data):
        if item_data == compain_data:
            print ('YES there are the same. {0}'.format(item_data))
        else:
            print ('they are NOT the same. Item data {0}, Campain data {1}'.format(item_data, compain_data))

