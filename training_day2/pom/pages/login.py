import time

from selenium.webdriver.common.keys import Keys

from training_day2.pom.text_codes.decorators import *

def login(driver):
    driver.find_element_by_xpath("//input[@type='email']").send_keys("",Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='password']").send_keys("",Keys.ENTER)

@invoke_browser
def login_only(driver):
    login(driver)