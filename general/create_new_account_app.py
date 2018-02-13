from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from datetime import datetime
import random


class CreateNewAccount(DriverConstructor):

    def tax_id(self):
        return self.driver.find_element(By.NAME, 'tax_id')

    def company(self):
        return self.driver.find_element(By.NAME, 'company')

    def first_name(self):
        return self.driver.find_element(By.NAME, 'firstname')

    def last_name(self):
        return self.driver.find_element(By.NAME, 'lastname')

    def address1(self):
        return self.driver.find_element(By.NAME, 'address1')

    def address2(self):
        return self.driver.find_element(By.NAME, 'address2')

    def post_code(self):
        return self.driver.find_element(By.NAME, 'postcode')

    def city(self):
        return self.driver.find_element(By.NAME, 'city')

    def email(self):
        return self.driver.find_element(By.NAME, 'email')

    def phone(self):
        return self.driver.find_element(By.NAME, 'phone')

    def desired_password(self):
        return self.driver.find_element(By.NAME, 'password')

    def confirm_password(self):
        return self.driver.find_element(By.NAME, 'confirmed_password')

    def submit(self):
        return self.driver.find_element(By.NAME, 'create_account')

    def news_letter(self):
        return self.driver.find_element(By.NAME, 'newsletter')

    def country_drop_down_element(self):
        return self.driver.find_element(By.XPATH, ".//span[@class='select2-selection__arrow']")

    def countries(self):
        self.country_drop_down_element().click()
        return self.driver.find_elements(By.CLASS_NAME, 'select2-results__option')

    def country(self):
        self.country_drop_down_element().click()
        ww=self.driver.find_elements(By.CLASS_NAME, 'select2-results__option')
        return ww[random.randrange(1, len(ww))]



    def zone_state(self):
        return self.driver.find_element_by_xpath("//select[@name='zone_code']")


    def zone_code(self):
        return self.driver.find_element(By.XPATH, "//*[@id='create-account']//select [@name='zone_code']/option[1]")


    def create_account(self):
        return self.driver.find_element(By.NAME, 'create_account')



# other

    def test_emailaddress(self):
        k = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        return 'test'+'_'+k+'@gmail.com'


    def create_new_account(self):
        self.tax_id().send_keys('123456')
        self.first_name().send_keys('test')
        self.last_name().send_keys('test')
        self.company().send_keys('test')
        self.country().click()
        if self.zone_state().get_attribute('disabled') == False :
            self.zone_code().click()
        self.address1().send_keys('test')
        self.post_code().send_keys('21021')
        self.city().send_keys('Boston')
        self.email().send_keys(self.test_emailaddress())
        self.phone().send_keys('123456789')
        self.desired_password().send_keys('Welcome1')
        self.confirm_password().send_keys('Welcome1')
        self.create_account().click()
        return self.test_emailaddress()

"""
def country_us(self):
    self.driver.find_element(By.XPATH, ".//span[@class='select2-selection__arrow']").click()
    list_of_countries = self.driver.find_elements(By.CLASS_NAME, 'select2-results__option')
    list_of_countries[224].click()
    return self.driver.find_element(By.XPATH, ".//*[@class='select2-selection__rendered']").get_attribute('title')

"""
