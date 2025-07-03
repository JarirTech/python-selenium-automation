# Created by Jarirtech at 7/3/2025


  Feature: Target help navigation

  Scenario: Help dropdown opens the Gift Cards topic page
    Given open the Target help page
    When  choose "Gift Cards" from the topic dropdown
    And click the "Gift Cards" button
    Then the URL contains "childcat=Target+GiftCard"