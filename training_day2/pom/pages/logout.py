import time

from training_day2.pom.text_codes.decorators import *
@invoke_browser
def logout(driver):
    driver = webdriver.Firefox()
    driver.find_element_by_xpath("//span[@class='gb_Ia gbii']").click()
    driver.find_element_by_xpath("//a[text()='Sign out']").click()