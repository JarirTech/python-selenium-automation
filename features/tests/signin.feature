# Created by JarirTech at 6/4/2025
Feature: test Target signin


  Scenario: verify that a logged out user can navigate to Sign In
    Given Open target main page
    When click on account button
    Then Click SignIn button from side navigation
    Then Verify SignIn page opened
