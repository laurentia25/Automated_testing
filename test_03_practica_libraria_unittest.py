"""Folosind libraria unittest, testeaza Heroku"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/login"
    LOGIN_BTN = (By.CLASS_NAME, 'radius')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    ALERT_USERNAME = (By.ID, 'flash')

    def setUp(self):
        """
        Defnim instructiunile pe care dorim
        sa le efectuam inainte de fiecare test
        Aceasta metoda se va apela de fiecare data
        inainte de rularea unui test
        """
        print("Inainte de rulare test")
        # instantierea browserului
        self.driver = webdriver.Edge()

        # accesarea link
        self.driver.get(self.LINK)

        # maximizarea ferestrei
        self.driver.maximize_window()

    def tearDown(self):
        """
        Instructiunile pe care dorim sa le efectuam
        dupa rularea fiecarui test.
        Aceasta metoda se va apela de fiecare data
        dupa de rularea unui test
         """
        print("Dupa rulare test")
        # inchidem browserul
        self.driver.quit()

        # Test 1
        # URL-ul este corect
    def test_current_url(self):
        print("Ruleaza test")
        actual_url = self.driver.current_url
        expected_url = self.LINK
        self.assertEqual(actual_url, expected_url, "Unexpected URL")

        # Test 2:
        # Verifica ca titlul paginii apare corect
    def test_page_title(self):
        print('Verificare titlu pagina')
        actual_title = self.driver.title
        expected_title = 'The Internet'
        self.assertEqual(actual_title, expected_title, 'Unexpected Title')

        # test 4:
        # Verifica ca butonul de login este pe site
    def test_check_login_btn(self):
        print('Verificare buton login')
        button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_BTN))
        if button.is_displayed:
            print('Butonul este vizibil')
        else:
            print('Butonul nu este vizibil')

        # test 5
        #  - username incorect + parola corect
    def test_login_func_1(self):
        print('Verificare functie logare cu username incorect + parola corecta')
        username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME))
        username.send_keys('wrong_username')
        password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys('SuperSecretPassword!')
        button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_BTN))
        button.click()
        alert = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ALERT_USERNAME))
        actual_alert = alert.text
        expected_alert = "Your username is invalid!"
        self.assertIn(expected_alert, actual_alert, "Different alert message!")

        #test 6
        # username corect + parola incorecta
    def test_login_func_2(self):
        print('Verificare functie logare cu username corect + parola incorecta')
        username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME))
        username.send_keys('tomsmith')
        password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys('IncorrectPassword!')
        button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_BTN))
        button.click()
        alert = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ALERT_USERNAME))
        actual_alert = alert.text
        expected_alert = "Your password is invalid!"
        self.assertIn(expected_alert, actual_alert, "Different alert message!")

        # test 7
        # username corect + parola corecta
    def test_login_func_3(self):
        print('Verificare functie logare cu username corect + parola corecta')
        username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME))
        username.send_keys('tomsmith')
        password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys('SuperSecretPassword!')
        button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_BTN))
        button.click()
        current_link = self.driver.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(current_link, expected_url, 'Unexpected URL')
