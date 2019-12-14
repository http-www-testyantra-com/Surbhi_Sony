from training_day2.pom.pages.login import *
from training_day2.pom.pages.homepage import *


@invoke_browser
def mail_test(a):
    login()
    HomePage.get_title()

mail_test("http://www.gmail.com")

