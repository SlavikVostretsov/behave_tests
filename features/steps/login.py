from behave import *
from selene.browser import *
from pages.login_page import Login

login_page = Login()

@given('I have opened login page')
def step_impl(context):
    open_url("/login")


@when('I login with "{username}" name and "{password}" password')
def step_impl(context, username, password):
    login_page.login(username, password)


@then('I see "{text}" text')
def step_impl(context, text):
    login_page.check_success_login(text)


@when('I refresh cookie')
def step_impl(context):
    driver().delete_all_cookies()
    driver().refresh()


@when('I login through the http with "{username}" name and "{password}" password')    
def step_impl(context, username, password):
    context.response = login_page.login_http(username, password)


@then('I should get "{response_code}" response code')
def step_impl(context, response_code):
    login_page.check_response_status(context.response["code"], int(response_code))


@then('I should get "{message}" message in the response')
def step_impl(context, message):
    login_page.check_response_message(context.response["message"], message)