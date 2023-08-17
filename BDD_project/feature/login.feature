Feature: Check the funtionality of login page
  # Scenariu 1: username corect + parola corect
  # Scenariu 2 username corect + parola incorecta
  # Scenariu 3 username incorect + parola corecta
  # Scenariu 4 username corect + parola none
  # Scenariu 5 username none + parola corecta
  # Scenariu 6 username none + parola none
  # Scenariu 7 username incorect + parola none
  # Scenariu 8 username none + parola incorect
  # Scenariu 9 username incorect + parola incorect
  # Scenariu 10 username blocat + parola corecta

  # Scenariu 1
  @skip
  Scenario: Succes login
    Given I am on the saucedemo login page
    When I insert the correct username and correct password
    And I click the login button
    Then I can login into the application and see the list of the products

   # Scenariu 2
    @skip
    Scenario: Check login func when username is valid, but password is incorrect
      Given I am on the saucedemo login page
      When I insert the correct username and incorrect password
      And I click the login button
      Then I cannot login into the aplication and receive error message:Epic sadface: Username and password do not match any user in this service

    # Scenariu 3
    @skip
    Scenario: Check login func when username is invalid, but password is correct
      Given I am on the saucedemo login page
      When I insert the incorrect username and correct password
      And I click the login button
      Then I cannot login into the aplication and receive error message:Epic sadface: Username and password do not match any user in this service

    # Scenariu 4
    @skip
    Scenario: Check login func when username is valid, but password in none
      Given I am on the saucedemo login page
      When I insert the correct username and none password
      And I click the login button
      Then I cannot login into the aplication and receive error message:Epic sadface: Password is required

     # Scenariu 5
    @skip
    Scenario: Check login func when username is none, but password in valid
      Given I am on the saucedemo login page
      When I insert none username and valid password
      And I click the login button
      Then I cannot login into the aplication and receive error message:Epic sadface: Username is required

     # Scenariu 6
    Scenario: Check login func when username is none, but password in valid
      Given I am on the saucedemo login page
      When I click the login button
      Then I cannot login into the aplication and receive error message:Epic sadface: Username is required
