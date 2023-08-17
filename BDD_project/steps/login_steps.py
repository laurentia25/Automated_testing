from behave import *


@given("I am on the saucedemo login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I insert the correct username and correct password")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_correct_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("I can login into the application and see the list of the products")
def step_impl(context):
    context.products_page.check_current_url()


@when("I insert the correct username and incorrect password")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_incorrect_password()


@when("I insert the incorrect username and correct password")
def step_impl(context):
    context.login_page.insert_incorrect_username()
    context.login_page.insert_correct_password()


@when("I insert the correct username and none password")
def step_impl(context):
    context.login_page.insert_correct_username()


@when('I insert none username and valid password')
def step_impl(context):
    context.login_page.insert_correct_password()


@then('I cannot login into the aplication and receive error message:Epic sadface: Username and password do not match any user in this service')
def step_impl(context):
    context.login_page.check_error_message()


@then('I cannot login into the aplication and receive error message:Epic sadface: Password is required')
def step_impl(context):
    context.login_page.check_error_msg_no_psw()


@then('I cannot login into the aplication and receive error message:Epic sadface: Username is required')
def step_impl(context):
    context.login_page.check_error_msg_no_username()


