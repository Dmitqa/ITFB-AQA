from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_laptop_product_compare_btn_visible(driver, click_laptop):
    path = (By.XPATH, "//*[@id='compare-total']/span")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(path))


def test_page_laptop_product_compare_btn_clickable(driver, click_laptop):
    element = driver.find_element(By.XPATH, "//*[@id='compare-total']/span")
    WebDriverWait(driver, 3).until(exp.element_to_be_clickable(element))


def test_page_laptop_product_compare_btn_text_in_script(driver, click_laptop):
    element = (By.XPATH, "//*[@id='compare-total']/span")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(element, "Product Compare"))


def test_page_laptop_product_sort_list_btn_visible(driver, click_laptop):
    element = (By.XPATH, "//button[@id='button-list']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_laptop_product_sort_grid_btn_visible(driver, click_laptop):
    element = (By.XPATH, "//button[@id='button-grid']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_laptop_product_sort_by_category_visible(driver, click_laptop):
    element = (By.XPATH, "//select[@id='input-sort']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_laptop_product_input_limit_category_visible(driver, click_laptop):
    element = (By.XPATH, "//select[@id='input-limit']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))
