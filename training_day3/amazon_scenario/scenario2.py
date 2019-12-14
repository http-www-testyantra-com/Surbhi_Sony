from selenium import webdriver

class Home_Page():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    def home_page(self):
        try:
            driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        except Exception as e:
            print(e)
        finally:
            print("successfully clicked")

Home_Page().home_page()