from selenium.webdriver.common.by import By
from driver_constructor import DriverConstructor
from selenium.common.exceptions import NoSuchElementException
from general.base_test import BaseTest

class LoginPage(DriverConstructor):

    def login_btn(self):
        return self.driver.find_element(By.NAME, 'login')

    def username_field(self):
        return self.driver.find_element(By.NAME, "username")

    def password_field(self):
        return self.driver.find_element(By.NAME, "password")

    def login(self, url, user, passw):
        # Change wait time to handle browser hang issue
        self.driver.implicitly_wait(30)

        print ("Open " + url)
        self.driver.get(url)

        self.username_field().send_keys(user)

        self.password_field().send_keys(passw)
        print ("into username field  " + format(user))
        print ("into password field  " + format(passw))

        print ("Click 'Login'")
        self.login_btn().click()

"""
        try:
            # Just look for Sign In field to check that page is loaded
            self.login_btn()
        except NoSuchElementException:
            print("No element")
            self.driver.refresh()

        # Set default timeout back
        self.driver.implicitly_wait(120)
        print ("Click 'Sign In'")
        self.login_btn().click()

        print ("Type '{0}' into username field".format(user))
        for i in user:
            self.username_field().send_keys(i)

        print ("Type '{0}' into password field".format(passw))
        for j in passw:
            self.password_field().send_keys(j)
    """
