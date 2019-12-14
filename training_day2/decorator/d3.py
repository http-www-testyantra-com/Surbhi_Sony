def invoke_brower(func):
    def inner(url):
        print("driver=webdriver.Chrome()")
        print("driver.get({})".format((url)))
        func("driver")
        print("driver.close()")

    return inner

@invoke_brower
def test_1(driver):
    print("testcase using", driver)

def test_2(driver):
    print("test case 2 using", driver)
test_1("http://www.gmail.com")
test_1("https://facebook.com")