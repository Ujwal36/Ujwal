import configparser
import os

from helpers.helper_web import get_browser

config = configparser.ConfigParser()

my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
# Reading the browser type from the configuration file for Selenium test automation
helper_func = get_browser(config.get('Environment', 'Browser'))
