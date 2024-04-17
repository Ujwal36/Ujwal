import time
from tokenize import String

from behave import given, then, when

import helpers.locators
import helpers.data


@given('I go to Equipmentshare Categories page')
def pagelaunch(context):
    launchURL = context.helperfunc.categoriesPageURL
    context.helperfunc.open(launchURL)
    context.helperfunc.maximize()


@then('I validate the page title to be {title}')
def validateTitle(context, title):
    actual_title = title
    current_title = str(context.helperfunc.find_page_title())
    assert current_title == actual_title


@then('I validate the URL to be {URL}')
def validateURL(context, URL):
    actual_URL = URL
    current_URL = str(context.helperfunc.find_page_URL())
    print(current_URL and actual_URL)
    assert actual_URL == current_URL


@then('I navigate to {solution} page and validate {URL} and {Title}')
def validatesolutionsPageURLAndTitles(context, solution, URL, Title):
    print(solution)
    print(URL)
    if solution == "core":
        CORE_SOLUTIONS = context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.CORE_SOLUTIONS)
        CORE_SOLUTIONS.click()
    elif solution == "advanced":
        ADVANCED_SOLUTIONS = context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.ADVANCED_SOLUTIONS)
        ADVANCED_SOLUTIONS.click()
    else:
        TOOLING_SOLUTIONS = context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.TOOLING_SOLUTIONS)
        TOOLING_SOLUTIONS.click()

    validateURL(context, URL)
    validateTitle(context, Title)


@then('I validate the primary header section')
def validatePrimaryHeaderSection(context):
    EquipmentShare_Logo = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.ESLOGO)
    RENT = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.RENT)
    BUY = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.BUY)
    SERVICE = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.SERVICE)
    T3_TECH = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.T3_TECH)
    CAREERS = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.CAREERS)
    LOCATIONS = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.LOCATIONS)
    SEARCH = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.SEARCH)
    CONTACT = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.CONTACT)
    CONTACT_NUM = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.CONTACT_NUM)
    User = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.User)
    Cart = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.CART)

    assert EquipmentShare_Logo.is_displayed() is True
    assert RENT.text == "RENT"
    assert BUY.text == "BUY"
    assert SERVICE.text == "SERVICE"
    assert T3_TECH.text == "T3 TECH"
    assert CAREERS.text == "CAREERS"
    assert LOCATIONS.text == "LOCATIONS"
    assert SEARCH.is_displayed() is True
    assert CONTACT.is_displayed() is True
    assert CONTACT_NUM.text == "1.888.80.RENTS"
    assert User.is_displayed() is True
    assert Cart.is_displayed() is True


@then('I validate the secondary header section')
def validateSecondaryHeaderSection(context):
    LOCATION = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageSecondaryHeadersLocators.Location)
    CORE_SOLUTIONS = context.helperfunc.find_by_id(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.CORE_SOLUTIONS)
    ADVANCED_SOLUTIONS = context.helperfunc.find_by_id(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.ADVANCED_SOLUTIONS)
    TOOLING_SOLUTIONS = context.helperfunc.find_by_id(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.TOOLING_SOLUTIONS)

    assert LOCATION.text == "Set Location For Accurate Pricing"
    assert CORE_SOLUTIONS.text == "CORE SOLUTIONS"
    assert ADVANCED_SOLUTIONS.text == "ADVANCED SOLUTIONS"
    assert TOOLING_SOLUTIONS.text == "TOOLING SOLUTIONS"


@then('I validate all the sections should have the products listed with images')
def validateCategoriesMainPageSectionProductImages(context):
    aerial_work_platforms = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Aerial_work_platforms).get_attribute('src')
    Agriculture_landscaping = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Agriculture_landscaping).get_attribute('src')
    Compaction = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageMainSection.Compaction).get_attribute(
        'src')
    Concrete_Masonry = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Concrete_Masonry).get_attribute('src')
    Climate_Control = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Climate_Control).get_attribute('src')
    Compressed_air = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Compressed_air).get_attribute('src')
    Fluid_solutions = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Fluid_solutions).get_attribute('src')
    Power_solutions = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Power_solutions).get_attribute('src')
    Industrial_Tooling = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Industrial_Tooling).get_attribute('src')
    Safety_testing_communication = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.Safety_testing_communication).get_attribute('src')

    assert aerial_work_platforms is not None
    assert Agriculture_landscaping is not None
    assert Compaction is not None
    assert Concrete_Masonry is not None
    assert Climate_Control is not None
    assert Compressed_air is not None
    assert Fluid_solutions is not None
    assert Power_solutions is not None
    assert Industrial_Tooling is not None
    assert Safety_testing_communication is not None


@then('I validate the sub-category under each category')
def validateSubCategoryUnderEachCategory(context):
    Aerial_work_platformsText = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Aerial_work_platforms_text).text
    Aerial_work_platforms_Category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Aerial_work_platforms_category).text
    assert Aerial_work_platforms_Category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Aerial_work_platformsText)

    Agriculture_landscaping_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Agriculture_landscaping_text).text
    Agriculture_landscaping_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Agriculture_landscaping_category).text
    assert Agriculture_landscaping_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Agriculture_landscaping_text)

    Compaction_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Compaction_text).text
    Compaction_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Compaction_category).text
    assert Compaction_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Compaction_text)

    Concrete_Masonry_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Concrete_Masonry_text).text
    Concrete_Masonry_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Concrete_Masonry_category).text
    assert Concrete_Masonry_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Concrete_Masonry_text)

    Climate_Control_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Climate_Control_text).text
    Climate_Control_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Climate_Control_category).text
    assert Climate_Control_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Climate_Control_text)

    Compressed_air_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Compressed_air_text).text
    Compressed_air_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Compressed_air_category).text
    assert Compressed_air_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Compressed_air_text)

    Fluid_solutions_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Fluid_solutions_text).text
    Fluid_solutions_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Fluid_solutions_category).text
    assert Fluid_solutions_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Fluid_solutions_text)

    Power_solutions_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Power_solutions_text).text
    Power_solutions_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Power_solutions_category).text
    assert Power_solutions_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Power_solutions_text)

    Industrial_Tooling_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Industrial_Tooling_text).text
    Industrial_Tooling_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Industrial_Tooling_category).text
    assert Industrial_Tooling_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Industrial_Tooling_text)

    Safety_testing_communication_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Safety_testing_communication_text).text
    Safety_testing_communication_category = context.helperfunc.find_by_xpath(
        helpers.locators.CategorySubcategoriesMapping.Safety_testing_communication_category).text
    assert Safety_testing_communication_category == helpers.data.PageRelatedData.category_subcategory_dict.get(
        Safety_testing_communication_text)


@given('I click on a category {subcategory}')
def SelectCategory(context, subcategory):
    self = helpers.locators.CategoriesPageMainSection
    var = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageMainSection.__getattribute__(self, subcategory))
    var.click()


@then('I validate the set location feature')
def validateSetlocationfFeature(context):
    context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).click()
    Location_search = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location_SearchInput)
    current_Location = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.current_location)
    Location_search_text = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Jobsite_Location_Text)

    assert Location_search.is_displayed()
    assert current_Location.text == "Use my current location".upper()
    assert Location_search_text.text == "Where is your jobsite?"


@then('I Click on location icon on the top left corner twice')
def ValidateLocationFeature(context):
    Bool = False
    context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).click()
    Location_search = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location_SearchInput)
    context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).click()

    try:
        Location_search.is_displayed()
    except Exception as exception_name:
        exception_name = type(exception_name).__name__
        assert exception_name is not None
        Bool = True
    finally:
        assert Bool


@then('I Click on location icon on the top left corner')
def Clicklocation(context):
    context.helperfunc.find_by_xpath(helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).click()


@then('I click on set location type "D" in the search text and I validate the search results')
def setlocation_validatelocationresults(context):
    Location_Text = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).text

    if Location_Text.lower() != "set location for accurate pricing":
        context.helperfunc.find_by_xpath(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.ChangeLocationButton).click()

    Location_search = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location_SearchInput)
    Location_search.send_keys("d")

    search_result1 = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result1).text
    search_result2 = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result2).text
    search_result3 = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result3).text
    search_result4 = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result4).text
    search_result5 = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result5).text

    assert search_result1.startswith("D")
    assert search_result2.startswith("D")
    assert search_result3.startswith("D")
    assert search_result4.startswith("D")
    assert search_result5.startswith("D")


@then('I select a location {location}')
def SelectLocationAndValidate(context, location):
    try:
        context.helperfunc.find_by_xpath(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result1).click()
        time.sleep(10)
    except:
        Location_Text = context.helperfunc.find_by_xpath(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).text

        if Location_Text.lower() != "set location for accurate pricing":
            context.helperfunc.find_by_xpath(
                helpers.locators.CategoriesPageSecondaryHeadersLocators.ChangeLocationButton).click()

        Location_search = context.helperfunc.find_by_xpath(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.Location_SearchInput)
        Location_search.send_keys(location)

        context.helperfunc.find_by_xpath(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.Search_result1).click()
        time.sleep(10)

    current_location = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).text
    assert current_location == location


@then('I refresh the page and validate the location again to be {location}')
def RefreshPageandValidateLocation(context, location):
    context.helperfunc.refresh()
    time.sleep(10)
    current_location = context.helperfunc.find_by_xpath(
        helpers.locators.CategoriesPageSecondaryHeadersLocators.Location).text
    assert current_location == location


@then('I Validate Breadcrumb to be {Expected_Breadcrumb}')
def ValidateBreadcrumb(context, Expected_Breadcrumb):
    Actual_Breadcrumb = ""

    breadcrumb_links = context.helperfunc.find_elements_by_xpath(helpers.locators.ListingPageSections.Breadcrumb_link1)
    for link in breadcrumb_links:
        Actual_Breadcrumb += str(link.text) + " / "
        if link.text.startswith("RENT") or link.text.startswith("EQUIPMENT"):
            assert link.get_attribute('href') == "https://www.equipmentshare.com/rent"

    breadcrumb_link = context.helperfunc.find_by_xpath(helpers.locators.ListingPageSections.Breadcrumb_link2)
    Actual_Breadcrumb += breadcrumb_link.text

    print(Actual_Breadcrumb)
    print(Actual_Breadcrumb)

    assert Expected_Breadcrumb == Actual_Breadcrumb


@then('I Validate product count in listing page')
def ValidateProductCount(context):
    ActualProductCount = context.helperfunc.find_by_id(helpers.locators.ListingPageSections.ActualProductCount).text
    productcount = int(ActualProductCount.strip("(,)"))

    if productcount > 20:
        ProductCountAndSeeMoreText = context.helperfunc.find_elements_by_xpath(
            helpers.locators.ListingPageSections.ProductCountAndSeeMore)

        for Textdata in ProductCountAndSeeMoreText:
            if Textdata.text.find("See more") != -1:
                assert Textdata.text == "See more..."
            else:
                assert Textdata.text == "Showing 20 of " + str(productcount)

    else:
        ProductCountAndSeeMoreText = context.helperfunc.find_by_xpath(
            helpers.locators.ListingPageSections.ProductCountAndSeeMore).text
        assert ProductCountAndSeeMoreText.find("See more...") == -1
        assert ProductCountAndSeeMoreText == "Showing " + str(productcount) + " of " + str(productcount)


@then('I validate Filter By Category Section in {subcategory}')
def ValidateFilterByCategorySection(context, subcategory):
    subcategory = subcategory.replace("_", " ")
    FilterByCategoryAndCategoryTitle = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.FilterByCategoryAndCategoryTitle)

    for Textdata in FilterByCategoryAndCategoryTitle:
        if Textdata.text.find("Filter") != -1:
            assert Textdata.text == "Filter by Category"
        else:
            assert Textdata.text.upper() == subcategory.upper()

    AllSubcategoryHyperlink = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.AllSubcategoryHyperlink)

    for Textdata in AllSubcategoryHyperlink:
        if Textdata.text.find("All") != -1:
            assert Textdata.text == "All "
        else:
            assert Textdata.text.upper() == subcategory.upper()

    SubCategoryHyperlinks = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.SubCategoryHyperlinks)

    for Textdata in SubCategoryHyperlinks:
        assert Textdata.text in helpers.data.PageRelatedData.List_of_subcategories_dict.get(subcategory.upper())

    # To validate the default Filter marker in Filter by category section
    FilterByCategoryFilterMarker = context.helperfunc.find_by_xpath(
        helpers.locators.ListingPageSections.FilterByCategoryFilterMarker)
    assert FilterByCategoryFilterMarker.get_attribute(
        'class') == helpers.locators.ListingPageSections.FilterMarkerClassName


@when('I click on {subcategory} in Filter By Category section')
def ClickonSubCategoryInFilterByCategorySection(context, subcategory):
    SubCategoryHyperlinks = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.SubCategoryHyperlinks)
    for Textdata in SubCategoryHyperlinks:
        if Textdata.text == subcategory:
            Textdata.click()
            break


@then('I validate the items in the listing page for {subcategory}')
def ValidateListingPageItemsForSubCategory(context, subcategory):
    ListPageMainTitleHeading = context.helperfunc.find_by_xpath(
        helpers.locators.ListingPageSections.ListPageMainTitleHeading).text
    assert ListPageMainTitleHeading.lower() == subcategory.lower()
    ValidateProductCount(context)

    # validating Sub category name in the product card heading
    ProductCardsMainTitle = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.ProductCardsMainTitle)
    for names in ProductCardsMainTitle:
        assert names.text.lower() == subcategory.lower()

    # validating Equipment names in the product card
    subcategory_Beginning_Text = subcategory.split(" ")
    ProductCardEquipmentName = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.ProductCardEquipmentName)

    for names in ProductCardEquipmentName:
        assert names.text.lower().startswith(subcategory_Beginning_Text[0].lower())

    # Validating pricing for all the equipments
    EquipmentPricinginDollars = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.EquipmentPricinginDollars)
    for prices in EquipmentPricinginDollars:
        assert prices.text.startswith("$")

    # Validating pricing categories for all the equipments
    EquipmentPricingRanges = context.helperfunc.find_elements_by_xpath(
        helpers.locators.ListingPageSections.EquipmentPricingRanges)
    loopindex = 0
    for categories in EquipmentPricingRanges:
        loopindex += 1

        if loopindex % 3 == 1:
            assert str(categories.text.strip()) == "/ day"
        elif loopindex % 3 == 2:
            assert str(categories.text) == "/ week"
        else:
            assert str(categories.text) == "/ 4-week"


@when('I select the first equipment displayed in list page')
def SelectFirstEquipmentInListPage(context):
    context.helperfunc.find_by_xpath(
        helpers.locators.ListingPageSections.ProductCardEquipmentName).click()


@then('I validate the equipment name to be {equipmentname} and validate equipment pricing in details page')
def ValidateDetailsPageEquipmentDetails(context, equipmentname):
    EquipmentName = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.EquipmentName)

    assert EquipmentName.text.lower() == equipmentname.lower()

    EquipmentPricing = context.helperfunc.find_elements_by_xpath(
        helpers.locators.DetailsPageSections.PricingInDollars)

    for price in EquipmentPricing:
        assert price.text.startswith("$")
    # Validating pricing categories for all the equipments
    EquipmentPricingRanges = context.helperfunc.find_elements_by_xpath(
        helpers.locators.DetailsPageSections.PricingRange)
    loopindex = 0
    for categories in EquipmentPricingRanges:
        loopindex += 1

        if loopindex % 3 == 1:
            assert str(categories.text) == "/ day"
        elif loopindex % 3 == 2:
            assert str(categories.text) == "/ week"
        else:
            assert str(categories.text) == "/ 4-week"
    ValidateProductImage(context)


def ValidateProductImage(context):
    productImage = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.ProductImage)
    assert productImage.get_attribute('src') is not None
    assert str(productImage.get_attribute('src')).endswith(".jpeg")

def ValidateQuantityComponentDefaultValues(context):
    # Validating Default values
    quantityText = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.Quantity).text
    assert quantityText == "Quantity"

    QuantityIcrementerDecrementerButtondisplay = context.helperfunc.find_elements_by_xpath(
        helpers.locators.DetailsPageSections.QuantityIcrementerDecrementerButton)
    assert QuantityIcrementerDecrementerButtondisplay[0].text == "-"
    assert QuantityIcrementerDecrementerButtondisplay[1].text == "+"

    QuantityValue = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.QuantityValue).get_attribute(
        'value')
    assert QuantityValue == "1"

def ValidateIncrementDecrementByOne(context):
    # Validating Increment and decrement buttons
    QuantityIcrementerDecrementerButton = context.helperfunc.find_elements_by_xpath(
        helpers.locators.DetailsPageSections.QuantityIcrementerDecrementerButton)

    # Increment by 1 and validate

    QuantityIcrementerDecrementerButton[1].click()

    QuantityValue = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.QuantityValue).get_attribute(
        'value')
    assert QuantityValue == "2"

    # Decrement by 1 and validate

    QuantityIcrementerDecrementerButton[0].click()

    QuantityValue = context.helperfunc.find_by_xpath(helpers.locators.DetailsPageSections.QuantityValue).get_attribute(
        'value')
    assert QuantityValue == "1"

@then("I validate quantity component in details page")
def ValidateQuantityComponentDetailsPage(context):
    ValidateQuantityComponentDefaultValues(context)
    ValidateIncrementDecrementByOne(context)



