import time
from training_day2.pom.base.base import BasePage

from training_day2.pom.text_codes.decorators import *

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    @invoke_browser
    def get_title(self, driver):
        e_title = "Gmail"
        a_title = driver.tile()
        print(a_title)
        assert a_title == e_title, print("not in same page")
        print("in same page")

    @invoke_browser
    def inbox(self, driver):
        total_inbox = driver.find_element_by_xpath("//div[@class='bsU']").text
        print(total_inbox)

    @invoke_browser
    def header_text(self, driver):
        headers = driver.find_elements_by_xpath(
            "//tr[@class='zA zE']/descendant::td[@id=':2z']/descendant::span[@class='bqe']").text
        for i in headers:
            print(i.text)

    @invoke_browser
    def check_box_click(self, driver):
        driver.find_element_by_xpath("//span[@role='checkbox']").click()
