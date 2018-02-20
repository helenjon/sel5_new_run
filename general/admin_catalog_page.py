from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from selenium.webdriver.support.ui import Select
from datetime import datetime
import random




class AdminCatalogPage(DriverConstructor):

    def add_new_product_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a[2]')




class AddNewProduct(DriverConstructor):

    def save_add_new_product(self):
        return self.driver.find_element(By.NAME, 'save')

#general tab
    def general_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'General')


    def status(self):
        return self.driver.find_element(By.XPATH, "//input[@name='status' and @value='1']")

    def name(self):
        return self.driver.find_element(By.NAME, 'name[en]')


    def code(self):
        return self.driver.find_element(By.NAME, 'code')


    def categories_list(self):
        return self.driver.find_elements(By.XPATH, '//input[@name="categories[]"]')


    def product_groups_gender_list(self):
        return self.driver.find_elements(By.XPATH, "//input[@name='product_groups[]']")


    def quantity(self):
        return self.driver.find_element(By.NAME, 'quantity')


    def upload_image(self, upload_file_product_pic):
        self.driver.find_element(By.NAME, 'new_images[]').send_keys(upload_file_product_pic)


    def date_valid_from(self):
        return self.driver.find_element(By.XPATH, "//input[@name='date_valid_from']")


    def date_valid_to(self):
        return self.driver.find_element(By.XPATH, "//input[@name='date_valid_to']")


# information tab
    def information_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Information')


    def select_manufacturer(self):
        Select(self.driver.find_element_by_name('manufacturer_id')).select_by_value('1')


    def keywords(self):
        return self.driver.find_element(By.NAME, 'keywords')

    def short_description(self):
        return self.driver.find_element(By.NAME, 'short_description[en]')


#prices tab
    def prices_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Prices')


    def purchase_prices(self):
        return self.driver.find_element(By.NAME, 'purchase_price')


    def select_purchase_price_currency_code(self):
        Select(self.driver.find_element_by_name('purchase_price_currency_code')).select_by_value('USD')




#other

#every time new code for creating newly created product
    def code_new(self):
        return datetime.now().strftime('%m%d%H%M%S')

    def get_random_category_from_list(self):
        ww=self.categories_list()
        return ww[random.randrange(1, len(ww))]

    def get_random_product_groups_gender(self):
        ww=self.product_groups_gender_list()
        return ww[random.randrange(1, len(ww))]


    def get_random_quantity_number(self):
        return random.randrange(1, 10)



