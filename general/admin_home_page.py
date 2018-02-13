from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from selenium.common.exceptions import NoSuchElementException



class AdminHomePage(DriverConstructor):

    def main_menu_links(self):
        return self.driver.find_elements(By.XPATH, '//*[@id="app-"]/a')

    def main_menu_podcatalog_links(self):
        return self.driver.find_elements(By.XPATH, ".//ul[@class='docs']/li/a/span")

    def exceptionn(self):
        try:
            self.driver.find_element(By.TAG_NAME, 'h1')
            return 'pass'
        except NoSuchElementException:
            return 'No such thing'

    def main_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'logotype')

    def countries_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Countries')


    def list_of_countries(self):
        return self.driver.find_elements(By.XPATH, ".//*[@id='content']/form/table/tbody/tr/td[@style]/a")





    def click_countries_link(self):
        print ('Click Countries')
        self.countries_link().click()

    def list_of_subzones(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody/tr/td[6]")

    def list_of_edit_property(self):
        return self.driver.find_elements(By.XPATH, "//a[@title='Edit']")



#sub-zone page

    def list_sub_zone_web_elements(self):
        return self.driver.find_elements(By.XPATH, ".//*[@id='table-zones']/tbody/tr/td[3]")

# other

    def get_list_of_someother_names(self, list_of_something):
        list_of_someother_names = []
        for i in range(len(list_of_something)):
            list_of_someother_names.append(list_of_something[i].get_attribute("textContent"))
        return list_of_someother_names

    def sorted_or_not(self, list_of_names):
        sorted_list_of_names = sorted(list_of_names)
        for i in range(len(list_of_names)):
            if sorted_list_of_names != list_of_names:
                return 'Not alphabet'
            return 'Alphabet'

