"""
1. Navigheaza catre urmatorul LINK: https://demo.nopcommerce.com/
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

# accesare link

LINK = "https://demo.nopcommerce.com/"
driver.get(LINK)
time.sleep(1)
# maximizam fereastra
driver.maximize_window()
time.sleep(1)

"""
2. Verifica ca titlul paginii este cel asteptat.
"""

actual = driver.title
expected = "nopCommerce demo store"

assert expected == actual

"""
3. Da click pe Register
"""

register_element = driver.find_element(By.LINK_TEXT, "Register")
register_element.click()
time.sleep(1)

"""
4. Selecteaza un gen (sectiunea Gender).
Verifica ca elementul gasit are atributul type cu valoarea 'radio'
"""
gender_element = driver.find_element(By.ID, "gender-female")
assert gender_element.get_attribute('type') == "radio"

gender_element.click()
time.sleep(2)

"""
5. Identifica elementul in care putem scrie prenumele.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un prenume.
"""

first_name_input = driver.find_element(By.ID, "FirstName")
tag = first_name_input.tag_name
assert tag == "input"
first_name_input.send_keys("Laurentia")
time.sleep(2)

"""
6. Identifica elementul in care putem scrie numele de familie.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un nume de familie.
"""

last_name_input = driver.find_element(By.ID, "LastName")
tag = last_name_input.tag_name
assert tag == "input"
last_name_input.send_keys("Vasilasco")
time.sleep(2)

"""
7. Identifica elementul in care putem scrie email-ul.
Verifica ca valoarea atributului name este cea asteptata.
Completeaza cu o adresa de email.
"""
email_input = driver.find_element(By.ID, "Email")
assert email_input.get_attribute("name") == "Email"
import random
email_input.send_keys(f"user{random.randint(1, 99999)}@yahoo.com")
time.sleep(2)

"""
8. Identifica elementele in care trebuie sa introduci parolele
si introdu aceeasi parola (3 caractere) in ambele locuri.
Verifica ca apare mesajul de eroare asteptat.
"""
pwd_element = driver.find_element(By.ID, "Password")
pwd_element.send_keys("abc")

confirm_pwd_element = driver.find_element(By.ID, "ConfirmPassword")
confirm_pwd_element.send_keys("abc")

error_txt = driver.find_element(By.ID, "Password-error")
actual_msg = error_txt.text
expected_msg = "Password must meet the following rules:\nmust have at least 6 characters"
assert actual_msg == expected_msg
time.sleep(2)

"""
9. Sterge parolele introdusa la punctul 6.
Introdu o parola din 10 caractere.
Introdu o parola de confirmare care sa nu coincida cu cea initiala.
Apasa pe butonul REGISTER.
Verifica ca apare mesajul de eroare asteptat.
"""

pwd_element.clear()
confirm_pwd_element.clear()
time.sleep(2)

pwd_element.send_keys("0123456789")
confirm_pwd_element.send_keys("01234567812")
time.sleep(2)

register_btn = driver.find_element(By.ID, "register-button")
register_btn.click()
time.sleep(1)
error_match = driver.find_element(By.ID, "ConfirmPassword-error")
error_match_msg = error_match.text
expected_match_msg = "The password and confirmation password do not match."
assert error_match_msg == expected_match_msg
time.sleep(2)

"""
10. Sterge continutul introdus la parole de la punctul 7
Introdu doua parole identice si apasa pe butonul REGISTER.
Verifica ca in url-ul paginii curente se gaseste string-ul 
"registerresult"
"""

pwd_element.clear()
confirm_pwd_element.clear()

pwd_element.send_keys("0123456789")
confirm_pwd_element.send_keys("0123456789")

print(f"Before: {driver.current_url}")
register_btn = driver.find_element(By.ID, "register-button")
register_btn.click()


current_url = driver.current_url
print(f"After: {driver.current_url}")

assert "registerresult" in current_url
time.sleep(2)

"""
11. Inchide browser-ul.
"""
driver.quit()

