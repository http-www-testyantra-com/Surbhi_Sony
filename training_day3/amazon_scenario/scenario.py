import time

from selenium import webdriver

from training_day3.amazon_scenario.custom_exception import *

class OpenBrowser():

    def open_browser(self):
        global driver
        browser = input("enter browser")
        try:
            if browser == "Chrome":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Firefox()
        except Exception as e:
            print(e)
            raise NameException()
        finally:
            OpenBrowser.open_browser()

OpenBrowser.open_browser()