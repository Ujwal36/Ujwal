import os
from configparser import ConfigParser

from helpers.helper_web import get_browser


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func

    # Local Chrome WebDriver
    # if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()

    def after_all(context):
        context.helperfunc.close()
