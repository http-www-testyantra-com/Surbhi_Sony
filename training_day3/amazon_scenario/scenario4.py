import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class Scenario4():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def move_to_element(self):
        act = ActionChains(driver)
        try:
            elements = driver.find_element_by_xpath("//span[text()='Electronics']")
            act.move_to_element(elements).perform()
            time.sleep(3)
            driver.find_element_by_xpath("(//a[text()='Mi'])[1]").click()
        except Exception as e:
            print(e)
            print("done")

Scenario4.move_to_element()