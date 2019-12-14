from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.driver.getTitle()
            return "actualTitle is verified"
        except:
            return "title not verified"

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        else:
            return By.LINK_TEXT
        return False

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            return "element not found"
        return element

    def clearText(self,locator,locatorType):
        self.getElement(locator , locatorType).clear()


    def elementClick(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            print("element not clickable")

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except:
           return "cannot send keys"
