import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Scenario33():
    def original(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.bluestone.com")
        driver.find_element_by_xpath("//input[@placeholder='Search for Jewellery']").send_keys("Rings", Keys.ENTER)
        all_original_price = driver.find_elements_by_xpath(
            "//span[@class='b-price-wrapper']/descendant::span[@id='bst-actual-price']")
        original_price = []
        discounted_price = []
        a = [i for i in all_original_price]
        for i in a:
            o_price = i.text
            # o_price.replace(",","")
            original_price.append(o_price[3:])
        all_discounted_price = driver.find_elements_by_xpath(
            "//span[@class='b-price-wrapper']/descendant::span[@id='bst-discounted-price']")
        b = [i for i in all_discounted_price]
        for i in b:
            d_price = i.text
            # d_price.replace(",","")
            discounted_price.append(d_price[3:])
        price = []
        original = list(map(lambda x: x.replace(",", ""), original_price))
        discounted = list(map(lambda x: x.replace(",", ""), discounted_price))
        print(original)
        print(discounted)
        for i in range(len(original)):
            p = int(original[i]) - int(discounted[i])
            price.append(p)

Scenario33().original()