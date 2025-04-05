from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_main_cart_btn_visible(driver):
    xpath = (By.XPATH, '//div[@id="header-cart"]/div/button')
    cart_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert cart_btn.is_displayed()


def test_page_main_cart_btn_clickable(driver):
    xpath = (By.XPATH, '//div[@id="header-cart"]/div/button')
    cart_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    exp_message = driver.find_element(By.XPATH, '//div[@id="header-cart"]//li')
    cart_btn.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="header-cart"]//li')))
    assert exp_message.text == "Your shopping cart is empty!"


def test_page_main_navbar_panel_visible(driver):
    xpath = (By.XPATH, '//nav[@id="menu"]')
    navbar_panel = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located(xpath))
    assert navbar_panel.is_displayed()


def test_page_main_text_in_h3(driver):
    tag = (By.TAG_NAME, 'h3')
    h3_title = driver.find_element(*tag)
    WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element(tag, "Featured"))
    assert h3_title.text == "Featured"


def test_page_main_currency_euro_invisible(driver):
    xpath = (By.XPATH, "//a[@href='EUR']")
    euro = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.invisibility_of_element_located(xpath))
    assert not euro.is_displayed()


def test_page_main_elem_attr_placeholder(driver):
    xpath = (By.XPATH, '//div[@id="search"]/input')
    search_field = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.element_attribute_to_include(xpath, "placeholder"))
    assert search_field.get_attribute("placeholder") == 'Search'
