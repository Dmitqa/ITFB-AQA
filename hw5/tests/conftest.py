import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.firefox.service import Service as FoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--url", default="http://localhost:80", action="store")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "Chrome":
        driver = webdriver.Chrome(service=ChromService())
    elif browser == "Firefox":
        driver = webdriver.Firefox(service=FoxService())
    else:
        driver = webdriver.Edge(service=EdgeService())

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    yield driver
    driver.close()


@pytest.fixture(scope="module")
def click_laptop(driver):
    driver.get("http://localhost/en-gb/catalog/laptop-notebook")
    return driver


@pytest.fixture(scope="module")
def page_login(driver):
    driver.get("http://localhost/en-gb?route=account/login")
    return driver


@pytest.fixture(scope="module")
def page_register(driver):
    driver.get("http://localhost/en-gb?route=account/register")
    return driver
