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
  Background:
    Given I am on the saucedemo login page
#  # Scenariu 1
#  @skip
#  Scenario: Succes login
#    When I insert the correct username and correct password
#    And I click the login button
#    Then I can login into the application and see the list of the products
#
#   # Scenariu 2
#  @skip
#  Scenario: Check login func when username is valid, but password is incorrect
#    When I insert the correct username and incorrect password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service
#
#    # Scenariu 3
#  @skip
#  Scenario: Check login func when username is invalid, but password is correct
#    When I insert the incorrect username and correct password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service
#
#    # Scenariu 4
#    @skip
#  Scenario: Check login func when username is valid, but password in none
#    When I insert the correct username and none password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Password is required
#
#     # Scenariu 5
#
#  Scenario: Check login func when username is none, but password in valid
#    When I insert none username and valid password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username is required
#
#     # Scenariu 6
#    @skip
#  Scenario: Check login func when username is none, but password in none
#    When I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username is required
#
#     # Scenariu 7
#    @skip
#  Scenario: Check login func when username is invalid, but password is none
#    When I insert invalid username and none password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Password is required
#
#      # Scenariu 8
#    @skip
#  Scenario: Check login func when username is none, but password is invalid
#    When I insert none username and invalid password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username is required
#
#      # Scenariu 9
#    @skip
#  Scenario: Check login func when username is invalid, but password is invalid
#    When I insert invalid username and invalid password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service
#
#      # Scenariu 10
#    @skip
#  Scenario: Check login func when username is blocked, but password is valid
#    When I insert a blocked username and valid password
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Sorry, this user has been locked out.

# OPTIMIZARE SCENARII:
  Scenario: Check that we can login into the application when providing correct credentials
    When I insert the username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I can login into the application and see the list of the products

#  Scenario: Check that we can't login into the application when providing incorrect credentials
#    When I insert the username "invalid_username" and password "invalid_password"
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service
#
#  Scenario: Check that we can't login into the application when providing incorrect credentials
#    When I insert the username "none" and password "none"
#    And I click the login button
#    Then I cannot login into the application and receive error message:Epic sadface: Username is required

  Scenario Outline: Check that we can't login into the application when providing incorrect credentials
    When I insert the username "<username>" and password "<password>"
    And I click the login button
    Then I cannot login into the application and receive error message: "<error_msg>"
  Examples:
    | username | password | error_msg |
    | invalid_username| invalid_password | Epic sadface: Username and password do not match any user in this service |
    | none            | invalid_password | Epic sadface: Username is required                                        |
    | invalid_username| none             | Epic sadface: Password is required                                        |
    | none            | none             | Epic sadface: Username is required                                        |
    | locked_out_user | secret_sauce     | Epic sadface: Sorry, this user has been locked out.                       |
