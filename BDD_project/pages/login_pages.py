from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.TAG_NAME, "h3")

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def insert_correct_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("standart_user")

    def insert_incorrect_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("incorrect_user")

    def insert_correct_password(self):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys("secret_sauce")

    def insert_incorrect_password(self):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys("incorrectpass")

    def click_login_button(self):
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        login_btn.click()

    def check_error_message(self):
        expected_err = "Epic sadface: Username and password do not match any user in this service"
        error_msg = self.browser.find_element(*self.ERROR_MSG)
        actual_err = error_msg.text
        assert expected_err == actual_err

    def check_error_msg_no_psw(self):
        expected_err = 'Epic sadface: Password is required'
        error_msg = self.browser.find_element(*self.ERROR_MSG)
        actual_err = error_msg.text
        assert expected_err == actual_err

    def check_error_msg_no_username(self):
        expected_err = 'Epic sadface: Username is required'
        error_msg = self.browser.find_element(*self.ERROR_MSG)
        actual_err = error_msg.text
        assert expected_err == actual_err
