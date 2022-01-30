Feature: basket test

  Scenario: verify empty basket
    Given navigate to website
    And close the address selection
    When search for "Lale"
    And filter "kırmızı" color ones
    And select the first product
    And add product to basket
    And delete product from the basket
    Then verify homepage is open