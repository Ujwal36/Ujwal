from behave import given, then


@given('I go to Equipmentshare product details page')
def step(context):
    context.helperfunc.openbrowser('https://equipmentshare-us-7fcd6ee2fbc58ac5b15ef.webflow.io/equipment-classes'
                                   '/articulating-boom-lift-30-35ic')
    context.helperfunc.maximize()


@then('I validate the page title')
def step(context):
    actual_title = "Copy of EquipmentShare - Kickdrum"
    current_title = context.helperfunc.find_page_title()
    assert current_title == actual_title
    context.helperfunc.close()


@then('I validate the equipment name')
def step(context):
    context.helperfunc.close()


@then('I validate the equipment price')
def step(context):
    context.helperfunc.close()
