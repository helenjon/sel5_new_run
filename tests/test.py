from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random


def get_list_of_availbale_product_size(driver, list_of_availbale_product_size):
    list_of_available_product_size = []
    i = 1
    for all in list_of_availbale_product_size[1:]:
        list_of_available_product_size.append(all.get_attribute('value'))
        print all.get_attribute('value')
    return list_of_available_product_size


def select_product_size(driver, product_size, list_of_availbale_product_size):
    select = Select(product_size)
    list_of_availbale_product_size = get_list_of_availbale_product_size(driver, list_of_availbale_product_size)
    selcted_value = list_of_availbale_product_size[random.randrange(0, len(list_of_availbale_product_size))]
    print selcted_value
    select.select_by_value(selcted_value)


driver=webdriver.Chrome()
driver.get("http://localhost:8081/litecart/en/rubber-ducks-c-1/subcategory-c-2/test1-p-7")
product_size= driver.find_element(By.NAME, "options[Size]")
list_of_availbale_product_size= driver.find_elements(By.XPATH, "//select[@name='options[Size]']/option")
select_product_size(driver, product_size, list_of_availbale_product_size)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkout').click()


