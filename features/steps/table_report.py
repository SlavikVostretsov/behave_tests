from behave import *
from selene.browser import *
from pages.table_report_page import TableReport

table_report_page = TableReport()

@given('I have opened table report page')
def step_impl(context):
    open_url("/table")


@then('I see total amount of the products for every quarter')   
def step_impl(context):
    table_report_page.check_total_amount_for_each_quarter()


@then('I see total amount of the products for every year')   
def step_impl(context):
    table_report_page.check_total_amount_for_year()