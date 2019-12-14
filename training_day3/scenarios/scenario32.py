from selenium import webdriver

class Scenario32():
    def store_locator(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.bluestone.com")
        driver.find_element_by_xpath("//span[text()='Locate']").click()
        places = driver.find_elements_by_xpath("//ul[@class='side-bar']/li")
        print("no of location are: ", len(places))

Scenario32().store_locator()