Feature: case study

  Scenario: verify login
    Given navigate to website
    And close the address selection
    When open sign in page
    And enter email "seleniumtester102@gmail.com" and password "test@102"
    Then verify homepage is open

  Scenario: verify product in the basket
    When open shop by category
    And select guitar
    And randomly select a submenu
    And randomly select a product
    And open the product in new tab
    And add product the cart
    And close the tab
    And open the basket
    Then product should be seen in the basket
