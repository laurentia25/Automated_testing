"""
1.
- Instantiaza un browser de Edge.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
LINK = "https://the-internet.herokuapp.com/"
driver.get(LINK)
time.sleep(2)
driver.maximize_window()

"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""

form_element = driver.find_element(By.LINK_TEXT, "Form Authentication")
form_element.click()
time.sleep(2)

"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""

title = driver.find_element(By.TAG_NAME, "h2")
actual_txt = title.text
expected_txt = "Login Page"

assert expected_txt == actual_txt
time.sleep(2)

"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""
username = driver.find_element(By.ID, "username")
pwd = driver.find_element(By.ID, "password")
username.send_keys("tomsmith")
pwd.send_keys("SuperSecretPassword!")
time.sleep(2)
button = driver.find_element(By.CLASS_NAME, "radius")
button.click()
time.sleep(1)

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

current_link = driver.current_url
expected_link = "https://the-internet.herokuapp.com/secure"

assert current_link == expected_link

"""
6. Da click pe butonul logout
"""
logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
logout_btn.click()
time.sleep(1)

"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""
username = driver.find_element(By.ID, "username")
pwd = driver.find_element(By.ID, "password")
username.send_keys("tomsmith")
pwd.send_keys("1234")
button = driver.find_element(By.CLASS_NAME, "radius")
button.click()

error = driver.find_element(By.ID, "flash")
error_txt = error.text
print(error_txt)
actual_error = "Your password is invalid!\n×"
assert error_txt == actual_error
time.sleep(1)
"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este 
[parola]"
"""

potential_pwd = driver.find_element(By.TAG_NAME, "h4")
potential_pwd_txt = potential_pwd.text
pwds = potential_pwd_txt.split()
for pwd in pwds:
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    parola = driver.find_element(By.ID, "password")
    parola.send_keys(pwd)
    button = driver.find_element(By.CLASS_NAME, "radius")
    button.click()
    if driver.current_url == "https://the-internet.herokuapp.com/secure":
        print(f'Parola secreta este {pwd}')
        break
else:
    print(f"Nu am reusit sa gasesc parola")