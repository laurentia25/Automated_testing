# SAPTMANA 3 - part 3

##  📝 OBIECTIVE
- WORKSHOP - continuare proiect BDD
- Background
- Parametrizare scenario steps
- Scenario outline
- Generare raport HTML scenarii de test

## 🔶 Background
- Daca consider ca un pas given (contextul actiunii)
este valabil pentru mai multe scenarii/pentru toate scenariile,
atunci, pentru a economisi cod voi putea trece
acel pas la inceputul unui feature file sub keyword-ul
Background.
```
Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the saucedemo login page
    When I insert username "standard_user" and password "secret_sauce"
    When I click the login button
    Then I can login into the application and see the list of products
```

```
Feature: Check the functionality of the login page

    Background:
        Given I am on the saucedemo login page
        
    Scenario: Check that you can login into the application when providing correct credentials
        When I insert username "standard_user" and password "secret_sauce"
        When I click the login button
        Then I can login into the application and see the list of products
```

## 🔶 Parametrizare scenario steps
- Atunci cand avem pasi asemanatori in diferite scenarii si doar valorile introduse/testate difera,
putem sa parametrizam pasul respectiv.

1. In feature file:
```
Scenario: look up a book
  Given I search for a valid book
   Then the result page will include "success"

Scenario: look up an invalid book
  Given I search for a invalid book
   Then the result page will include "failure"
```

2. In implementarea scenario step:

```
@then('the result page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))
```

## 🔶 Scenario Outline
- Cand avem scenarii de testare asemanatoare,
in care difera doar parametrii din pasi si rezultatul,
ne putem folosi de Scenario Outline pentru a rula
acelasi scenariu cu mai multe seturi de parametri.

```
Scenario Outline: Blenders
   Given I put "<thing>" in a blender,
    when I switch the blender on
    then it should transform into "<other thing>"

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |
```

## 🔶 Generare raport HTML

- Pentru a genera un raport HTML cu rezultatele testelor,
rulam comanda:

```commandline
behave -f html -o behave-report.html
```

- Inainte de a rula comanda, trebuie sa cream (la nivelul)
proiectului, un fisier "behave.ini", cu urmatorul continut
```
[behave.formatters]
html = behave_html_formatter:HTMLFormatter 
```
