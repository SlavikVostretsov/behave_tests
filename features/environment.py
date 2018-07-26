from selene.browsers import BrowserName
from selene import config
from behave.log_capture import capture
import os, time
from selene.browser import *
from allure_commons.types import AttachmentType
import allure


def before_all(context):
    config.browser_name = BrowserName.CHROME
    config.timeout = 15
    config.base_url = "http://testing-ground.scraping.pro"


@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join('error_shots', 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        driver().save_screenshot(scenario_file_path)
        allure.attach(driver().get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)