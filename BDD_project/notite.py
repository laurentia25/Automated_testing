"""
1. Folderul FEATURES:
- va contine fisierele descriptive cu extensia .feature
- in fisierele .feature, vom scrie, folosind limbajul Gherkin, scenariile de testare
- vom avea cate un fisier .feature pentru fiecare feature pe care dorim sa il testam
(ex: login, adaugare produse in cos, creare comenzi, cautare produse etc)
- pentru fiecare fisier .feature vom scrie mai multe scenarii (SCENARIO)
- un SCENARIO va avea un titlu/descriere si mai multi pasi
- pasii dintr-un scenariu pot fi GIVEN, WHEN, THEN, AND si BUT
- implementarea fiecarui pas dintr-un scenariu se va gasi in folderul steps


2. Folderul STEPS:
- va contine fisiere python cu implementarea pasilor din scenarii (.feature)
- pentru a implementa functionalitatea pasilor respectivi se va folosi, o librarie, numita behave
- instalare: pip install behave
- implementarea unui pas va fi inclusa intr-o functie denumita conventional step_impl,
care va fi decorata cu un decorator de forma: @step_type("<step description from .feature>")
- functia aceasta va lua in mod obligatoriu un parametru pe care
il denumim context
- acest context este o entitate pe care vom seta o serie de proprietati, de obicei in fisierul
environment.py

Exemple:

@given("I am on the login page")
def step_impl(context):
    pass

@when("I enter a valid email")
def step_impl(context):
    pass

3. Fisierul environment.py
- aici vom avea definite mai multe functii prin care vom modifica contextul astfel incat
sa definim instructiunile necesare a fi indeplinite inainte de rularea testelor si dupa
rularea testelor.

4. Fisierul browser.py:
- se mai poate denumi si driver.py
- definim o clasa numita Browser (Driver), care va avea metode si proprietati specifice interactiunii
cu browser-ul/driver-ul (deschiderea browser-ului, setare implicit wait, maximizare fereastra, inchidere browser etc)

5. Fisierul base_page.py:
- vom avea o clasa BasePage care va mosteni din clasa Browser si va cuprinde proprietati si caracteristici de baza
ale unei pagini web + interactiuni de baza pe o pagina web
(ex: identificarea unui element HTML, verificarea unui mesaj de eroare etc )

6. Folderul pages:
- vom avea clase definite pentru fiecare pagina din aplicatia web pe care o testam
- fiecare clasa va fi in propriul sau fisier.
(LoginPage, ProductPage, ProductsPage etc).
- fiecare clasa va mosteni din clasa BasePage.

"""