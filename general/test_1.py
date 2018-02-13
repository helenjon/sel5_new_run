# coding: utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from general.admin_home_page import AdminHomePage
import unicodedata
import mysql.connector
from home_app_page import HomeAppPage
from create_new_account_app import CreateNewAccount

def compare(item_data, compain_data):
    if item_data == compain_data:
        print ('YES there are the same. {0}'.format(item_data))
    else:
        print ('they are NOT the same. Item name {0}, Campain name {1}'.format(item_data, compain_data))


from selenium import webdriver

driver=webdriver.Chrome()
admin_url ='http://localhost:8081/litecart/en/'
driver.get(admin_url)
query = ()
cur = connection.cursor()
cur.execute("SELECT table_name FROM information_schema.tables "
            " WHERE table_type='BASE TABLE' "
            "AND table_schema='myschema'")
cur.execute("SHOW TABLES FROM litecart")

"""

def test1():
    dictionaries=[]
    #campaing list item information
    campaign_list = driver.find_elements(By.XPATH, "//*[@id='box-campaigns']/div//a[@class='link']")
    campaign_list_names = driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//div[@class='name']")
    campaign_list_manufacturers = driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//div[@class='manufacturer']")
    campaign_list_regular_prices = driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//s[@class='regular-price']")
    campaign_list_campaign_prices =driver.find_elements(By.XPATH, "//*[@id='box-campaigns']//strong[@class='campaign-price']")

    #creating list with dictionaries
    for i in range (len(campaign_list)):
        dictionaries.append('dictionary_name')
    print dictionaries

    #adding campaing list item information to the dictionary
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
        print dictionaries[i]

    #opening all campaign items in new tabs
    for i in range (len(campaign_list)):
       campaign_list[i].send_keys(Keys.CONTROL + Keys.RETURN)


    #run through the tabs and comparing the data
    for i in range(len(campaign_list)):
        driver.switch_to.window(driver.window_handles[-1])
        item_name = driver.find_element(By.XPATH, "//h1[@itemprop='name']").get_attribute('textContent')
    # in case Manufacturer not defined
        try:
            item_manufacturer = driver.find_element(By.XPATH, "//div[@class='manufacturer']/a/img").get_attribute('title')
        except NoSuchElementException:
            item_manufacturer = ''
        item_regular_price = driver.find_element(By.XPATH, "//div[@class='information']//s[@class='regular-price']")
        item_campaign_price = driver.find_element(By.XPATH, "//div[@class='information']//strong[@class='campaign-price']")
    # --------------------------
        item_regular_price1 = item_regular_price.get_attribute('textContent')
        item_campaign_price1 = item_campaign_price.get_attribute('textContent')
        item_colour_regular_prices = item_regular_price.value_of_css_property('color')
        item_font_size_regular_prices = item_regular_price.value_of_css_property('font-size')
        item_font_weight_regular_prices =item_regular_price.value_of_css_property('font-weight')
        item_colour_campaign_price = item_campaign_price.value_of_css_property('color')
        item_font_size_campaign_price = item_campaign_price.value_of_css_property('font-size')
        item_font_weight_campaign_price = item_campaign_price.value_of_css_property('font-weight')

    #---
        compare(item_name,dictionaries[i]['name'])
    # if manufacturer not defined on home page >> campaign it's sgous as empty sumbol in unicode
        compare(item_manufacturer, unicodedata.normalize("NFKD", dictionaries[i]['manufacturer']))
        compare(item_regular_price1, dictionaries[i]['regular_prices'])
        compare(item_campaign_price1, dictionaries[i]['campaign_prices'])

        compare(item_colour_regular_prices, dictionaries[i]['colour_regular_prices'])
        compare(item_font_size_regular_prices, dictionaries[i]['font_size_regular_prices'])
        compare(item_font_weight_regular_prices, dictionaries[i]['font_weight_regular_prices'])
        compare(item_colour_campaign_price , dictionaries[i]['color_campaign_price'] )
        compare(item_font_size_campaign_price, dictionaries[i]['font_size_campaign_price'])
        compare(item_font_weight_campaign_price, dictionaries[i]['font_weight_campaign_price'])

        driver.close()






