Feature: login test

  Scenario: verify login
    Given navigate to website
    And close the address selection
    When open sign in page
    And enter email "seleniumtester102@gmail.com" and password "test@102"
    Then verify homepage is open