from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_laptop_product_compare_btn_visible(driver, click_laptop):
    xpath = (By.XPATH, '//a[@id="compare-total"]')
    compare_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert compare_btn.is_displayed()


def test_page_laptop_product_compare_btn_clickable(driver, click_laptop):
    xpath = (By.XPATH, '//a[@id="compare-total"]')
    compare_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    compare_btn.click()
    assert driver.current_url == "http://localhost/en-gb?route=product/compare"
    driver.back()


def test_page_laptop_product_compare_btn_text_in_script(driver, click_laptop):
    xpath = (By.XPATH, "//a[@id='compare-total']/span")
    compare_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.text_to_be_present_in_element(xpath, "Product Compare"))
    assert compare_btn.text == "Product Compare (0)"


def test_page_laptop_product_sort_list_btn_visible(driver, click_laptop):
    xpath = (By.XPATH, "//button[@id='button-list']")
    sort_list_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert sort_list_btn.is_displayed()


def test_page_laptop_product_sort_grid_btn_visible(driver, click_laptop):
    xpath = (By.XPATH, "//button[@id='button-grid']")
    sort_grid_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert sort_grid_btn.is_displayed()


def test_page_laptop_product_sort_by_category_visible(driver, click_laptop):
    xpath = (By.XPATH, "//select[@id='input-sort']")
    sort_by_category = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert sort_by_category.is_displayed()


def test_page_laptop_product_sort_by_category_field_default(driver, click_laptop):
    xpath = (By.XPATH, '//select[@id="input-sort"]/option[1]')
    default_category = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert default_category.text == "Default" and default_category.is_displayed()
