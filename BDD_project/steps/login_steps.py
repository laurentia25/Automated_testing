from behave import *


@given("I am on the saucedemo login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


# @when("I insert the correct username and correct password")
# def step_impl(context):
#     context.login_page.insert_correct_username()
#     context.login_page.insert_correct_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("I can login into the application and see the list of the products")
def step_impl(context):
    context.products_page.check_current_url()


# @when("I insert the correct username and incorrect password")
# def step_impl(context):
#     context.login_page.insert_correct_username()
#     context.login_page.insert_incorrect_password()
#
#
# @when("I insert the incorrect username and correct password")
# def step_impl(context):
#     context.login_page.insert_incorrect_username()
#     context.login_page.insert_correct_password()
#
#
# @when("I insert the correct username and none password")
# def step_impl(context):
#     context.login_page.insert_correct_username()
#
#
# # scenariu 5
# @when('I insert none username and valid password')
# def step_impl(context):
#     context.login_page.insert_correct_password()
#
#
# @then('I cannot login into the application and receive error message:Epic sadface: Username is required')
# def step_impl(context):
#     context.login_page.check_error_msg_no_username()
#
#
# # Scenariu 7
# @when('I insert invalid username and none password')
# def step_impl(context):
#     context.login_page.insert_incorrect_username()
#
#
# @then('I cannot login into the application and receive error message:Epic sadface: Password is required')
# def step_impl(context):
#     context.login_page.check_error_msg_no_psw()
#
# # Scenariu 8
# @when('I insert none username and invalid password')
# def step_impl(context):
#     context.login_page.insert_incorrect_password()
#
#
# # Scenariu 9
# @when('I insert invalid username and invalid password')
# def step_impl(context):
#     context.login_page.insert_incorrect_username()
#     context.login_page.insert_incorrect_password()
#
#
# @then('I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service')
# def step_impl(context):
#     context.login_page.check_error_message()
#
#
# # Scenariu 10
# @when('I insert a blocked username and valid password')
# def step_impl(context):
#     context.login_page.insert_blocked_username()
#     context.login_page.insert_correct_password()

#
# @then('I cannot login into the application and receive error message:Epic sadface: Sorry, this user has been locked out.')
# def step_impl(context):
#     context.login_page.check_msg_blocked_user()


@when('I insert the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)

@then('I cannot login into the application and receive error message: "{error_msg}"')
def step_impl(context, error_msg):
    context.login_page.check_err_msg(error_msg)