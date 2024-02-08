import time

from behave import given, then

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
    assert actual_URL == current_URL


@then('I validate the primary header section')
def validatePrimaryHeaderSection(context):
    EquipmentShare_Logo = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.ESLOGO)
    RENT = context.helperfunc.find_by_xpath(helpers.locators.CategoriesPagePrimaryHeadersLocators.RENT)
    BUY = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.BUY)
    SERVICE = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.SERVICE)
    T3_TECH = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.T3_TECH)
    COMPANY = context.helperfunc.find_by_id(helpers.locators.CategoriesPagePrimaryHeadersLocators.COMPANY)
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
    assert COMPANY.text == "COMPANY"
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


@then('I validate the page url after clicking {solution} to be {url}')
def validatePageURLAfterClickingSecondaryHeaders(context, solution, url):
    if solution == "core solutions":
        context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.CORE_SOLUTIONS).click()
        validateURL(context, url)
    elif solution == "advanced solutions":
        context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.ADVANCED_SOLUTIONS).click()
        validateURL(context, url)
    else:
        context.helperfunc.find_by_id(
            helpers.locators.CategoriesPageSecondaryHeadersLocators.TOOLING_SOLUTIONS).click()
        validateURL(context, url)


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

@then('I Validate Breadcrumb and titles and product count')
def ValidateBreadcrumb(context):
    pass