from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class CategoriesPagePrimaryHeadersLocators(object):
    ESLOGO = '//img[@alt="Equipmentshare logo"]'
    RENT = '//div[@class = "es_p1-dropdown-toggle es_p1-menu"]'
    BUY = 'w-dropdown-toggle-1'
    SERVICE = 'w-dropdown-toggle-2'
    T3_TECH = 'w-dropdown-toggle-3'
    COMPANY = 'w-dropdown-toggle-7'
    LOCATIONS = 'w-dropdown-toggle-8'
    SEARCH = 'search-input'
    CONTACT = 'contact-button'
    CONTACT_NUM = '//a[@id="contact-button"]/div'
    User = '//img[@alt="User"]'
    CART = 'esr-cart-header-dropdown'

class CategoriesPageSecondaryHeadersLocators(object):
    Location = '//*[@id="esr-navbar-location-button"]/div/button'
    CORE_SOLUTIONS = 'core-solutions-link'
    ADVANCED_SOLUTIONS = 'advanced-solutions-link'
    TOOLING_SOLUTIONS = 'tooling-solutions-link'
    Location_SearchInput = '//input[@class="css-yxliqm"]'
    Jobsite_Location_Text = '//p[@class="MuiTypography-root MuiTypography-body1 css-p8n97r"]'
    current_location = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-1du6qyn"]'
    Search_result1 = '//div[@class="MuiBox-root css-1k95m2w"]/li/ul[1]'
    Search_result2 = '//div[@class="MuiBox-root css-1k95m2w"]/li/ul[2]'
    Search_result3 = '//div[@class="MuiBox-root css-1k95m2w"]/li/ul[3]'
    Search_result4 = '//div[@class="MuiBox-root css-1k95m2w"]/li/ul[4]'
    Search_result5 = '//div[@class="MuiBox-root css-1k95m2w"]/li/ul[5]'


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
    Aerial_work_platforms_category = CategoriesPageMainSection.Aerial_work_platforms + '/following::div[1]/div[1]'
    Aerial_work_platforms_text = CategoriesPageMainSection.Aerial_work_platforms + '/following::div[1]/div[2]'
    Agriculture_landscaping_category =  CategoriesPageMainSection.Agriculture_landscaping + '/following::div[1]/div[1]'
    Agriculture_landscaping_text = CategoriesPageMainSection.Agriculture_landscaping + '/following::div[1]/div[2]'
    Compaction_category = CategoriesPageMainSection.Compaction + '/following::div[1]/div[1]'
    Compaction_text = CategoriesPageMainSection.Compaction + '/following::div[1]/div[2]'
    Concrete_Masonry_category = CategoriesPageMainSection.Concrete_Masonry + '/following::div[1]/div[1]'
    Concrete_Masonry_text = CategoriesPageMainSection.Concrete_Masonry + '/following::div[1]/div[2]'
    Climate_Control_category = CategoriesPageMainSection.Climate_Control + '/following::div[1]/div[1]'
    Climate_Control_text = CategoriesPageMainSection.Climate_Control + '/following::div[1]/div[2]'
    Compressed_air_category = CategoriesPageMainSection.Compressed_air + '/following::div[1]/div[1]'
    Compressed_air_text = CategoriesPageMainSection.Compressed_air + '/following::div[1]/div[2]'
    Fluid_solutions_category = CategoriesPageMainSection.Fluid_solutions + '/following::div[1]/div[1]'
    Fluid_solutions_text = CategoriesPageMainSection.Fluid_solutions + '/following::div[1]/div[2]'
    Power_solutions_category = CategoriesPageMainSection.Power_solutions + '/following::div[1]/div[1]'
    Power_solutions_text = CategoriesPageMainSection.Power_solutions + '/following::div[1]/div[2]'
    Industrial_Tooling_category = CategoriesPageMainSection.Industrial_Tooling + '/following::div[1]/div[1]'
    Industrial_Tooling_text = CategoriesPageMainSection.Industrial_Tooling + '/following::div[1]/div[2]'
    Safety_testing_communication_category = CategoriesPageMainSection.Safety_testing_communication + '/following::div[1]/div[1]'
    Safety_testing_communication_text = CategoriesPageMainSection.Safety_testing_communication + '/following::div[1]/div[2]'


