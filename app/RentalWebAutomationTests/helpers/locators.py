from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class CategoriesPagePrimaryHeadersLocators(object):
    ESLOGO = '//img[@alt="Equipmentshare logo"]'
    RENT = '//div[@class = "es_p1-dropdown-toggle es_p1-menu"]'
    BUY = 'w-dropdown-toggle-1'
    SERVICE = 'w-dropdown-toggle-2'
    T3_TECH = 'w-dropdown-toggle-3'
    CAREERS = 'w-dropdown-toggle-7'
    LOCATIONS = 'w-dropdown-toggle-8'
    SEARCH = 'autocomplete-input'
    CONTACT = 'contact-button'
    CONTACT_NUM = '//a[@id="contact-button"]/div'
    User = '//img[@alt="User"]'
    CART = 'esr-cart-header-dropdown'

class CategoriesPageSecondaryHeadersLocators(object):
    Location = '//*[@id="esr-navbar-location-button"]/div/button[text()]'
    CORE_SOLUTIONS = 'core-solutions-link'
    ADVANCED_SOLUTIONS = 'advanced-solutions-link'
    TOOLING_SOLUTIONS = 'tooling-solutions-link'
    Location_SearchInput = '//div[@class="MuiBox-root css-1xta8wn"]/div/input'
    ChangeLocationButton = '//p[@class="MuiTypography-root MuiTypography-body1 css-1am7h2s"]'
    Jobsite_Location_Text = '//p[@class="MuiTypography-root MuiTypography-body1 css-p8n97r"]'
    current_location = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-1qyc0b7"]'
    LocationSearch_results = '//ul[contains(@class,"autocomplete-dropdown-item")]/span[text()]'
    UseMyCurrentLocation_Failure_Errors = current_location + '/preceding::p'

class CategoriesPageMainSection(object):
    Aerial_work_platforms = '//img[@alt="Aerial Work Platforms available for rent at EquipmentShare"]'
    Agriculture_landscaping = '//img[@alt="Utility Vehicle 4 - 6 Passenger, Gas"]'
    Compaction = '//img[@alt="Compaction available for rent at EquipmentShare"]'
    Concrete_Masonry = '//img[@alt="Saw Concrete 20 Walk-Behind Gas"]'
    Climate_Control = '//img[@alt="Climate Control available for rent at EquipmentShare"]'
    Compressed_air = '//img[@alt="Compressed Air available for rent at EquipmentShare"]'
    Fluid_solutions = '//img[@alt="Fluid Solutions available for rent at EquipmentShare"]'
    Power_solutions = '//img[@alt="Power Solutions"]'
    Industrial_Tooling = '//img[@alt="Industrial Tooling available for rent at EquipmentShare"]'
    Safety_testing_communication = '//img[@alt="Safety, Testing, and Communication"]'

class CategorySubcategoriesMapping(object):
    Aerial_work_platforms_category = CategoriesPageMainSection.Aerial_work_platforms + '/parent::div/following-sibling::div/p'
    Aerial_work_platforms_text = CategoriesPageMainSection.Aerial_work_platforms + '/parent::div/following-sibling::div/h3'
    Agriculture_landscaping_category =  CategoriesPageMainSection.Agriculture_landscaping + '/parent::div/following-sibling::div/p'
    Agriculture_landscaping_text = CategoriesPageMainSection.Agriculture_landscaping + '/parent::div/following-sibling::div/h3'
    Compaction_category = CategoriesPageMainSection.Compaction + '/parent::div/following-sibling::div/p'
    Compaction_text = CategoriesPageMainSection.Compaction + '/parent::div/following-sibling::div/h3'
    Concrete_Masonry_category = CategoriesPageMainSection.Concrete_Masonry + '/parent::div/following-sibling::div/p'
    Concrete_Masonry_text = CategoriesPageMainSection.Concrete_Masonry + '/parent::div/following-sibling::div/h3'
    Climate_Control_category = CategoriesPageMainSection.Climate_Control + '/parent::div/following-sibling::div/p'
    Climate_Control_text = CategoriesPageMainSection.Climate_Control + '/parent::div/following-sibling::div/h3'
    Compressed_air_category = CategoriesPageMainSection.Compressed_air + '/parent::div/following-sibling::div/p'
    Compressed_air_text = CategoriesPageMainSection.Compressed_air + '/parent::div/following-sibling::div/h3'
    Fluid_solutions_category = CategoriesPageMainSection.Fluid_solutions + '/parent::div/following-sibling::div/p'
    Fluid_solutions_text = CategoriesPageMainSection.Fluid_solutions + '/parent::div/following-sibling::div/h3'
    Power_solutions_category = CategoriesPageMainSection.Power_solutions + '/parent::div/following-sibling::div/p'
    Power_solutions_text = CategoriesPageMainSection.Power_solutions + '/parent::div/following-sibling::div/h3'
    Industrial_Tooling_category = CategoriesPageMainSection.Industrial_Tooling + '/parent::div/following-sibling::div/p'
    Industrial_Tooling_text = CategoriesPageMainSection.Industrial_Tooling + '/parent::div/following-sibling::div/h3'
    Safety_testing_communication_category = CategoriesPageMainSection.Safety_testing_communication + '/parent::div/following-sibling::div/p'
    Safety_testing_communication_text = CategoriesPageMainSection.Safety_testing_communication + '/parent::div/following-sibling::div/h3'


class ListingPageSections(object):
    Breadcrumb_link1 = '//*[@class="esr-breadcrumb esr-breadcrumb-link"]'
    Breadcrumb_link2 = '//div[@class="esr-breadcrumb esr-breadcrumb-disabled"][last()]'
    ListPageMainTitleHeading = '//h1[@class="esr-section-title-2"]'
    ActualProductCount = 'esr-equipment-list-total-count'
    ProductCountAndSeeMore = '//div[@id="esr-equipment-list"]/div/div/p[text()]'
    FilterByCategoryAndCategoryTitle = '//div[@class="esr-cp-filter-card"]/*[text()]'
    AllSubcategoryHyperlink = '//div[@class="esr-cp-filter-card"]/div/*[text()]'
    SubCategoryHyperlinks = '//a[@id="w-node-fad8d56b-85f0-06b9-3cda-1d3d63707ae9-62830260"]'
    ProductCardsMainTitle = '//div[@id="w-node-_6f0e3465-bdaf-6545-85e2-0d1a8e17c596-8e17c593"]/p'
    ProductCardEquipmentName = '//div[@id="w-node-_6f0e3465-bdaf-6545-85e2-0d1a8e17c596-8e17c593"]/h2'
    FilterByCategoryFilterMarker = '//a[text()="All "]/preceding-sibling::div'
    FilterMarkerClassName = 'esr-cp-filter-marker'
    EquipmentPricinginDollars = '//p[@class="MuiTypography-root MuiTypography-body1 price-cell-typography css-1aq3u9w"]'
    EquipmentPricingRanges = '//p[@class="MuiTypography-root MuiTypography-body1 price-cell-typography css-1aq3u9w"]/parent::div/following-sibling::p'

class DetailsPageSections(object):
    EquipmentName = '//div[@id="w-node-c693dd9c-22ea-d3c8-9a43-1e768e379fcc-62830264"]/h1'
    PricingInDollars = '//p[@class="MuiTypography-root MuiTypography-body1 price-cell-typography css-1aq3u9w"]'
    PricingRange = '//p[@class="MuiTypography-root MuiTypography-body1 price-cell-typography css-1irpbtm"]'
    ProductImage = '//div[@class="esr-pd-image-gallery-block tab-n-desktop"]/img'
    Quantity = '//p[@class="MuiTypography-root MuiTypography-body1 css-anuy18"]'
    QuantityIcrementerDecrementerButton = '//div[@class="MuiBox-root css-129k8e9"]/button/p'
    QuantityValue = '//input[contains(@class,"MuiInputBase-input MuiOutlinedInput-input") and @type="number"]'
    AddToCartButton = '//button[text()="Add to cart"]'

class AddToCartModal(object):
    AddToCartButton = '//button[text()="ADD TO CART"]'
    QuantityIcrementerDecrementerButton = '//button[@class ="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium quantity-update-button increment-button css-1tx175w"]'
    QuantityValue = '//input[contains(@class,"MuiInputBase-input MuiOutlinedInput-input") and @type="number"]'
    EquipmentName = '//div[contains(@class,"MuiBox-root css-19u2w0e")]/p'










