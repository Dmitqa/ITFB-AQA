import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.common.by import By
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
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(service=ChromService(), options=options)
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        driver = webdriver.Firefox(service=FoxService(), options=options)
    else:
        options = webdriver.EdgeOptions()
        options.add_argument('headless')
        driver = webdriver.Edge(service=EdgeService(), options=options)

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    yield driver
    driver.close()


@pytest.fixture(scope="module")
def click_laptop(driver):
    element = driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[2]/a")
    element.click()
    laptop_element = driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[2]/div/a")
    return laptop_element.click()


@pytest.fixture(scope="module")
def click_hp_lp_3065(driver):
    driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[2]/div/a").click()
    return driver.find_element(By.XPATH, "//*[@id='product-list']/div[1]/div/div[1]/a/img").click()


@pytest.fixture(scope="module")
def page_login(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'My Account')]").click()
    return driver.find_element(By.XPATH, "//*[@id='top']//a[contains(text(), 'Login')]").click()


@pytest.fixture(scope="module")
def page_register(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'My Account')]").click()
    return driver.find_element(By.XPATH, "//*[@id='top']//a[contains(text(), 'Register')]").click()
