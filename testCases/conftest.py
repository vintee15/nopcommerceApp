from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver= webdriver.Chrome()
        print("chrome browser is launching.......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching firefox.......")
    else:
        driver = webdriver.Ie()

    yield driver
    driver.quit()
    # return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######################## Pytest HTML report ##############
# It is hook for adding environment info in HTML report
def pytest_configure(config):
    if hasattr(config, "metadata"):
        config.metadata['Project Name'] = 'nop commerce'
        config.metadata['Module Name'] = 'Customers'
        config.metadata['Tester'] = 'vintee'
    else:
        print("⚠️ Warning: 'config.metadata' not available. Skipping metadata.")

# It is hook for delete or modify environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



