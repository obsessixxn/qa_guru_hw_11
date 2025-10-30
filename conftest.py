import pytest
from selene import browser, Config, Browser
from selenium import webdriver
from utils import attach


@pytest.fixture()
def options_for_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor="https:selenoid.autotests.cloud/wd/hub",
        options=options)
    browser = Browser(
        Config(
            driver=driver,
            timeout=10,
            window_width=1920,
            window_height=1080,
        )
    )
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNS": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    yield browser


    browser.quit()
