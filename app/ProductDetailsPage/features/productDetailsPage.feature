Feature: Testing Equipmentshare Product Details page

  Scenario: Test Launching and Headers validation
    Given I go to Equipmentshare product details page
    Then I validate the page title
    Then I validate the equipment name
    Then I validate the equipment price


  Scenario: Test Launching and Headers validation
    Given I go to Equipmentshare product details page
    Then I validate if the search bar is visible with the name “Find equipment and solutions"
    Then I enter equipment details "Articulating boom lift" in search bar and validate the equipment name