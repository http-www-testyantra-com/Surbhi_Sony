from selenium import webdriver

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver=func(driver)

    return inner

