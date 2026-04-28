import os
import pytest

from utils.driver_factory import get_driver
from utils import logger




def pytest_addoption(parser):
    parser.addoption(
        "--lambdatest",
        action="store_true",
        default=False,
        help="Run tests on LambdaTest cloud instead of locally",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for local runs: chrome | firefox | edge",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )




@pytest.fixture(scope="function")
def driver(request):
    use_lt  = request.config.getoption("--lambdatest")
    browser = request.config.getoption("--browser")
    hl      = request.config.getoption("--headless")


    test_name = request.node.name.replace("_", " ").title()

    logger.info(f"Starting driver  →  LambdaTest={use_lt}  browser={browser}")

    _driver = get_driver(
        use_lambdatest=use_lt,
        test_name=test_name,
        browser=browser,
        headless=hl,
    )

    yield _driver


    if use_lt:
        outcome = "passed" if request.node.rep_call.passed else "failed"
        _driver.execute_script(f"lambda-status={outcome}")

    _driver.quit()
    logger.info("Driver closed.")


# Needed so the LT teardown can read the test result
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep     = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
