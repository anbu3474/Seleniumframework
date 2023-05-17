import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser..........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.............")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")

# ----------------------- PyTest HTML Report ---------------------------------
# It is hook for Adding Environment info to HTML Report


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Anbarasan'

# It is hook for Delete/Modify Environment info to HTML Report


@pytest.hookimpl
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
