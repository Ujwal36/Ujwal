Feature: Rental Web Automation

  Scenario: ES categories page launch, verification of home page and Title verification
    Given I go to Equipmentshare Categories page
    Then I validate the page title to be Equipment Rental | EquipmentShare - A Better Way To Rent
    Then I validate the URL to be https://www.equipmentshare.com/rent
    Then I validate the primary header section
    Then I validate the secondary header section


  Scenario Outline: Categories page check product categories.
    Given I go to Equipmentshare Categories page
    Then I navigate to <solution> page and validate <URL> and <Title>
    Examples:
      |solution  | URL                                                  | Title                                                           |
      |core      |https://www.equipmentshare.com/rent/solutions/core    | Core Solutions: Construction Equipment Rental \| EquipmentShare    |
      |advanced  |https://www.equipmentshare.com/rent/solutions/advanced| Advanced Solutions: Construction Equipment Rental \| EquipmentShare|
      |tooling   |https://www.equipmentshare.com/rent/solutions/tooling | Tooling Solutions: Construction Equipment Rental \| EquipmentShare |

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

  Scenario: Validate location navbar feature in category listing page.
    Given I go to Equipmentshare Categories page
    Given I click on a category Compaction
    Then I Validate product count in listing page
    Then I Click on location icon on the top left corner twice

  Scenario: Validate location navbar feature in category listing page.
    Given I go to Equipmentshare Categories page
    Given I click on a category Compaction
    Then I Click on location icon on the top left corner
    Then I click on set location type D in the search text and I validate the search results
    Then I select a location Dallas, TX
    Then I refresh the page and validate the location again to be Dallas, TX


  Scenario: Validate listing page
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    Then I Validate Breadcrumb to be RENT / EQUIPMENT / AERIAL WORK PLATFORMS
    Then I validate the page title to be Aerial Work Platforms Rental | EquipmentShare
    Then I Validate product count in listing page

  Scenario: Validate Filter by category section in the listing page
     Given I go to Equipmentshare Categories page
     Given I click on a category Aerial_work_platforms
     Then I validate Filter By Category Section in Aerial_work_platforms

  Scenario: Validate page URL Breadcrumb and equipment details when clicked on sub-category links.
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    When I click on Electric Boom Lift in Filter By Category section
    Then I validate the URL to be https://www.equipmentshare.com/rent/categories/electric-boom-lift
    Then I validate the items in the listing page for Electric Boom Lift

  Scenario: Validate page links for previous category page
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    When I click on Electric Boom Lift in Filter By Category section
    Then I Validate Breadcrumb to be RENT / EQUIPMENT / AERIAL WORK PLATFORMS / ELECTRIC BOOM LIFT

  Scenario: Product details page launch and validate the page details
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    When I click on Articulating Boom Lift in Filter By Category section
    When I select the first equipment displayed in list page
    Then I validate the page title to be Articulating Boom Lift, 30' - 35' IC Rental | EquipmentShare
    Then I validate the URL to be https://www.equipmentshare.com/rent/equipment-classes/articulating-boom-lift-30-ft-35-ft-ic
    Then I Validate Breadcrumb to be RENT / EQUIPMENT / AERIAL WORK PLATFORMS / ARTICULATING BOOM LIFT / ARTICULATING BOOM LIFT, 30' - 35' IC
    Then I validate the equipment name to be Articulating Boom Lift, 30' - 35' IC and validate equipment pricing in details page

  Scenario: Validate the product pricing after changing the location
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    When I click on Articulating Boom Lift in Filter By Category section
    Then I Click on location icon on the top left corner
    Then I select a location Dallas, TX
    Then I Click on location icon on the top left corner
    Then I select a location San Francisco, CA

  Scenario: Validate the quantity field in product details page
    Given I go to Equipmentshare Categories page
    Given I click on a category Aerial_work_platforms
    When I click on Articulating Boom Lift in Filter By Category section
    When I select the first equipment displayed in list page
    Then I validate quantity component in details page