from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Scenario():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def cart_to_payment(self):
        driver.find_element_by_id("twotabsearchtextbox").send_keys("nokia mobile", Keys.ENTER)
        driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()
        w = driver.window_handles
        driver.switch_to.window(w[1])
        driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
        add_to_cart= driver.find_element_by_xpath("//h1[@class='a-size-medium a-text-bold']").text
        assert "Added to Cart" in add_to_cart, print("not added")
        print("added")
        driver.find_element_by_xpath("//span[@id='nav-cart-count']").click()
        driver.find_element_by_xpath("//input[@value='Save for later']").click()
        driver.find_element_by_xpath("//input[@id='pp-yM-114']").click()
        driver.find_element_by_xpath("//div[@id='pp-yM-115']/descendant::input[@class='a-button-input a-button-text' and @type='submit']").click()

Scenario().cart_to_payment()



