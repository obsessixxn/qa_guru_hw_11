import os

import pytest
from selene import browser, Config, Browser
from selenium import webdriver
from utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def selenoid_browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def options_for_browser(request):

    options = webdriver.ChromeOptions()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '128.0',
        "selenoid:options": {
            "enableVideo": True,
            "enableVNS": True
        }
    }

    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser = Browser(
        Config(
            driver=driver,
            timeout=10,
            window_width=1920,
            window_height=1080,
        )
    )

    options.capabilities.update(selenoid_capabilities)
    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
