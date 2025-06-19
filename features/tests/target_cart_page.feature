# Created by JarirTech at 6/11/2025
  #HW7
Feature: testing the target cart


  Scenario: User can add a product to the cart
    Given open target main page
    When search for toys
    And click on Add to Cart button
    And confirm Add to Cart button from side bar
    And open cart page
    Then Verify cart has 1 item
