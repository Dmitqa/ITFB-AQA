from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_main_cart_btn_visible(driver):
    element = (By.XPATH, "//button[@type='button']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_main_cart_btn_clickable(driver):
    element = driver.find_element(By.XPATH, "//*[@id='header-cart']/div/button")
    WebDriverWait(driver, 3).until(exp.element_to_be_clickable(element))


def test_page_main_navbar_el_visible(driver):
    element = (By.XPATH, "//ul[@class='nav navbar-nav']")
    WebDriverWait(driver, 3).until(exp.visibility_of_all_elements_located(element))


def test_page_main_text_in_script(driver):
    element = (By.XPATH, "//div[@id='content']/h3")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(element, "Featured"))


def test_page_main_currency_euro_invisible(driver):
    element = (By.XPATH, "//a[@href='EUR']")
    WebDriverWait(driver, 3).until(exp.invisibility_of_element_located(element))


def test_page_main_number_of_windows(driver):
    WebDriverWait(driver, 3).until(exp.number_of_windows_to_be(1))


def test_page_main_elem_attr_placeholder(driver):
    element = (By.XPATH, "//*[@id='search']/input")
    WebDriverWait(driver, 3).until(exp.element_attribute_to_include(element, "placeholder"))
