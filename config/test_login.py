from general.login_page import LoginPage
from general.base_test import BaseTest
import pytest


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver, variables):
        self.login = LoginPage(driver)
        self.vars = variables

    def test_login_incorrect(self):
        user = "test"
        passw = "test"
        print ("Verify login error")

        print self.vars
        self.login.login(self.vars['admin_url'], user, passw)
        print ("Verify login error")



