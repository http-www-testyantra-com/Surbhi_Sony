from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Scenario():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def cart_to_payement(self):
        driver.find_element_by_id("twotabsearchtextbox").send_keys("nokia mobile", Keys.ENTER)
        driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()
        w = driver.window_handles
        driver.switch_to.window(w[1])
        driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
        add_to_cart= driver.find_element_by_xpath("//h1[@class='a-size-medium a-text-bold']").text
        assert "Added to Cart" in add_to_cart, print("not added")
        print("added")
        driver.find_element_by_xpath("//a[@id='hlb-ptc-btn-native']").click()
        driver.find_element_by_id("ap_email").send_keys("sur.darsh@gmail.com", Keys.ENTER)
        driver.find_element_by_id("ap_password").send_keys("nagarrajendra", Keys.ENTER)
        driver.find_element_by_xpath("//a[@class='a-declarative a-button-text ']").click()
        driver.find_element_by_xpath("//input[@value='Continue']").click()


Scenario().cart_to_payement()



