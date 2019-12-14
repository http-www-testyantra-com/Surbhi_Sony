import time

from selenium import webdriver

class Scenario3():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def click(self):
        try:
            time.sleep(4)
            driver.find_element_by_xpath("(//a[text()='VIEW ALL'])[1]").click()
        except Exception as e:
            print(e)
            print("click intercepted")
            driver.back()

Scenario3().click()