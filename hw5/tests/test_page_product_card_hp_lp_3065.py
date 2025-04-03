from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_hp_lp_3065_title_visible(driver, click_hp_lp_3065):
    path = (By.XPATH, "//h1")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(path))


def test_page_hp_lp_3065_title_text_in_script(driver, click_hp_lp_3065):
    element = (By.XPATH, "//h1")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(element, "HP LP3065"))


def test_page_hp_lp_3065_price_visible(driver, click_hp_lp_3065):
    element = (By.XPATH, "//span[@class='price-new']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_hp_lp_3065_add_to_card_btn_visible(driver, click_hp_lp_3065):
    element = (By.XPATH, "//*[@id='button-cart']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_hp_lp_3065_add_to_card_btn_clickable(driver, click_hp_lp_3065):
    element = driver.find_element(By.XPATH, "//*[@id='button-cart']")
    WebDriverWait(driver, 3).until(exp.element_to_be_clickable(element))


def test_page_hp_lp_3065_add_to_wishlist_btn_visible(driver, click_hp_lp_3065):
    element = (By.XPATH, "//*[@type='submit']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_hp_lp_3065_quantity_value_visible(driver, click_hp_lp_3065):
    element = (By.XPATH, "//*[@name='quantity']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))
