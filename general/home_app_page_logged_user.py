from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor


class HomeAppPageLoggedUser(DriverConstructor):

    def logout(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT  , 'Logout')