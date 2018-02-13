from general.login_page import LoginPage
from general.admin_home_page import AdminHomePage
from general.base_test import BaseTest
from selenium.webdriver.common.by import By
import pytest


class TestMainAdmin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver, variables):
        self.login = LoginPage(driver)
        self.vars = variables
        self.admin_home_page=AdminHomePage(driver)
        self.login.login(self.vars["admin_url"], self.vars["admin_login"], self.vars["admin_password"])





    def not_test_check_alphabetick_countries(self, driver):
    # sel-5  - task 9 Check sorting countries and sub-zone in admin http://software-testing.ru/lms/mod/assign/view.php?id=41868
        counter_zone = 0
        number_of_zones = []
        nonsorteditems = []


        self.admin_home_page.countries_link().click()
    #check whether countries in alphabet order
        list_of_countries1=self.admin_home_page.list_of_countries()
        print ('number of found countries = {} ').format(len(list_of_countries1))
        list_of_country_names1 = self.admin_home_page.get_list_of_someother_names(list_of_countries1)
        result = self.admin_home_page.sorted_or_not(list_of_country_names1)
        print ('sorted or not countries = {} ').format(result)

    # check which countries have subzones
        list_of_subzones1 = self.admin_home_page.list_of_subzones()
        print ('number of subzones = {} ').format(len(list_of_subzones1))
        list_of_edit_property1 = self.admin_home_page.list_of_edit_property()
        print ('number of edits = {} ').format(len(list_of_edit_property1))

    #get number of zones in sub-zone
        for i in range(len(list_of_subzones1)):
            zones = list_of_subzones1[i].get_attribute('innerText')
            #print ('zones = {} ').format(zones)
            number_of_zones.append(zones)

    #check whether zone have sub-zones
        for all in number_of_zones:
            #print ('all = {} ').format(all)
    # if zone have sub-zone - check for alphabet opder
            if all != '0':
                list_of_edit_property1[counter_zone].click()
                driver.implicitly_wait(10)
    #get list of web-elements of subzones
                list_sub_zone_web_elements1 = self.admin_home_page.list_sub_zone_web_elements()
                #print ('list_sub_zone_web_elements = {} ').format(list_sub_zone_web_elements1)
    #get list of zub-zones name
                list_of_sub_zone_names = self.admin_home_page.get_list_of_someother_names(list_sub_zone_web_elements1)
                print ('list_of_sub_zone_names = {} ').format(list_of_sub_zone_names)
    # check if those names in alphabet order
                result_subzone = self.admin_home_page.sorted_or_not(list_of_sub_zone_names[:-1])
                print ('sub_zone_names_sortd_non_sorted = {} ').format(result_subzone)

    # return to Countlies page
                self.admin_home_page.countries_link().click()
                list_of_edit_property1 = self.admin_home_page.list_of_edit_property()
                if result == 'Not alphabet':
                    nonsorteditems.append(list_of_country_names1[counter_zone])

            counter_zone = counter_zone + 1

        print ('nonsorteditems = {} ').format(nonsorteditems)
        assert len(nonsorteditems) == 0, 'all countries sorted alphabetiacally'

    def not_test_run_all_links_main_menu(self, driver):
    #sel-5  - task 7 - http://software-testing.ru/lms/mod/assign/view.php?id=41865
        links = self.admin_home_page.main_menu_links()
        links_len = len(links)
        print ('links len = {} ').format(links_len)
        i = 1
    #run through all list of links
        for i in range(links_len):
            links[i].click()
            print links[i], i
            podcatalog = self.admin_home_page.main_menu_podcatalog_links()
            print ('podcatalog list = {} ').format(podcatalog)
            j = 0
    #check if manu has sub-menu
            if len(podcatalog) > 0:
                print len(podcatalog)
                for j in range(len(podcatalog)):
                    podcatalog[j].click()
                    podcatalog = self.admin_home_page.main_menu_podcatalog_links()
                    print self.admin_home_page.exceptionn()

            else:
                 print self.admin_home_page.exceptionn()
            self.admin_home_page.main_link().click()
            driver.implicitly_wait(10)
            links = self.admin_home_page.main_menu_links()


    def test_add_to

