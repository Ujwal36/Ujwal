Feature: Testing Equipmentshare Categories page

  Scenario: ES categories page launch, verification of home page and Title verification
    Given I go to Equipmentshare Categories page
    Then I validate the page title to be Equipment Rental | EquipmentShare - A Better Way To Rent
    Then I validate the URL to be https://www.equipmentshare.com/rent
    Then I validate the primary header section
    Then I validate the secondary header section


  Scenario: Categories page check product categories.
    Given I go to Equipmentshare Categories page
    Then I validate the page url after clicking core solutions to be https://www.equipmentshare.com/rent#core-solutions
    Then I validate the page url after clicking advanced solutions to be https://www.equipmentshare.com/rent#advanced-solutions
    Then I validate the page url after clicking tooling solutions to be https://www.equipmentshare.com/rent#tooling-solutions

  Scenario: Categories page main page section
    Given I go to Equipmentshare Categories page
    Then I validate all the sections should have the products listed with images

  Scenario: Validate the name of the sub-categories under each category
    Given I go to Equipmentshare Categories page
    Then I validate the sub-category under each category


  Scenario: Validate the listing page upon clicking on any sub-category
    Given I go to Equipmentshare Categories page
    Given I click on a category Compaction
    Then I validate the page title to be Compaction Rental | EquipmentShare
    Then I validate the URL to be https://www.equipmentshare.com/rent/categories/compaction
    Then I validate the set location feature

  Scenario: Validate navbar feature in category listing page.
    Given I go to Equipmentshare Categories page
    Given I click on a category Compaction
    Then I Click on location icon on the top left corner twice

  Scenario: Validate navbar feature in category listing page.
    Given I go to Equipmentshare Categories page
    Given I click on a category Compaction
    Then I Click on location icon on the top left corner
    Then I click on set location type "D" in the search text and I validate the search results
    Then I select a location Dallas, TX
    Then I refresh the page and validate the location again to be Dallas, TX

  Scenario: Validate listing page
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    Then I Validate Breadcrumb and titles and product count
