# Created by JarirTech at 6/11/2025
Feature: test target search feature


  Scenario: user can search a product on target website
    Given Open target main page
    When search for phone
    Then verify that search for phone worked