import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from config.config import (
    BROWSER, HEADLESS, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT,
    LT_USERNAME, LT_ACCESS_KEY, LT_HUB_URL, LT_CAPABILITIES
)


def get_chrome_driver(headless=False):
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1366,768")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    if headless:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver


def get_edge_driver(headless=False):
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless")
    return webdriver.Edge(options=options)


def get_local_driver(browser=None, headless=None):
    b = (browser or BROWSER).lower()
    h = headless if headless is not None else HEADLESS
    if b == "chrome":
        driver = get_chrome_driver(h)
    elif b == "edge":
        driver = get_edge_driver(h)
    else:
        raise ValueError(f"'{b}' is not supported. use chrome or edge.")
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver


def get_lambdatest_driver(test_name=None):
    if not LT_USERNAME or not LT_ACCESS_KEY:
        raise EnvironmentError(
            "Add LT_USERNAME and LT_ACCESS_KEY to your .env file first."
        )
    caps = dict(LT_CAPABILITIES)
    if test_name:
        caps["LT:Options"] = {**caps["LT:Options"], "name": test_name}

    lt_options = ChromeOptions()
    lt_options.set_capability("browserName", caps["browserName"])
    lt_options.set_capability("browserVersion", caps["browserVersion"])
    lt_options.set_capability("LT:Options", caps["LT:Options"])

    driver = webdriver.Remote(
        command_executor=LT_HUB_URL,
        options=lt_options,
    )
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver


def get_driver(use_lambdatest=False, test_name=None, browser=None, headless=None):
    if use_lambdatest:
        return get_lambdatest_driver(test_name=test_name)
    return get_local_driver(browser=browser, headless=headless)