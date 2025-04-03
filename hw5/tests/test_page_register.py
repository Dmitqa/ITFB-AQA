from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_register_title_visible(driver, page_register):
    path = (By.XPATH, "//h1")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(path))


def test_page_register_title_text_in_script(driver, page_register):
    element = (By.XPATH, "//h1")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(element, "Register Account"))


def test_page_register_modal_window_visible(driver, page_register):
    element = (By.XPATH, "//div[@id='content']")
    WebDriverWait(driver, 3).until(exp.visibility_of_all_elements_located(element))


def test_page_register_field_name_visible(driver, page_register):
    element = (By.XPATH, "//*[@name='firstname']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_register_continue_btn_visible(driver, page_register):
    element = (By.XPATH, "//*[@type='submit']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_register_continue_btn_text_in_script(driver, page_register):
    element = (By.XPATH, "//*[@type='submit']")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(element, "Continue"))


def test_page_register_privacy_policy_check_box_visible(driver, page_register):
    element = (By.XPATH, "//*[@type='checkbox' and @name='agree']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))
