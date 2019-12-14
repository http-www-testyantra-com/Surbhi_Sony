from selenium import webdriver

class Scenario():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def switch_alert(self):
        try:
            driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
            alert = driver.switch_to.alert
            alert.dismiss()
        except Exception as e:
            print(e)
            print("no such alert pop-up")

Scenario().switch_alert()