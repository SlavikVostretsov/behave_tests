from selene.support.jquery_style_selectors import s
from selene import bys
import requests
from lxml import html


class Login(object):

    # def for elements
    def username(self):
        return s("#usr")

    def password(self):
        return s("#pwd")  

    def submit(self):
        return s("input[type='submit']")

    def message(self):
        return ".//*[@id='case_login']//h3/text()"

    # methods
    def login(self, username, password):
        self.username().set(username)
        self.password().set(password)
        self.submit().click()

    def get_Message(self):
        return s('#case_login h3').text

    def login_http(self, username, password):
        response = requests.post("http://testing-ground.scraping.pro/login?mode=login", data={"usr": username, "pwd": password})
        return {
            "message": html.fromstring(response.content).xpath(self.message())[0],
            "code": response.status_code
        }
