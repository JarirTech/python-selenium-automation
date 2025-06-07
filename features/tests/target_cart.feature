# Created by JarirTech at 6/4/2025
Feature: test target shopping cart


  Scenario: User can verify that target shopping cart is empty
    Given Open target main page
    When click on shopping cart icon
    Then shopping cart is empty