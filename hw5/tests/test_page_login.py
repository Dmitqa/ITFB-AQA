from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_login_modal_window_new_customer_visible(driver, page_login):
    element = (By.XPATH, "//*[@id='content']/div/div[1]/div")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_login_modal_window_new_customer_title_text_in_script(driver, page_login):
    element = (By.XPATH, "//*[@id='content']/div/div[1]/div/h2")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(
        element, "New Customer"))


def test_page_login_new_customer_continue_button_visible(driver, page_login):
    element = (By.XPATH, "//*[@id='content']//a[contains(text(), 'Continue')]")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_login_modal_window_returning_customer_visible(driver, page_login):
    element = (By.XPATH, "//*[@id='form-login']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_login_modal_window_returning_customer_title_text_in_script(driver, page_login):
    element = (By.XPATH, "//*[@id='form-login']/h2")
    WebDriverWait(driver, 3).until(exp.text_to_be_present_in_element(
        element, "Returning Customer"))


def test_page_login_returning_customer_email_field_visible(driver, page_login):
    element = (By.XPATH, "//*[@id='input-email']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_login_returning_customer_password_field_visible(driver, page_login):
    element = (By.XPATH, "//*[@id='input-password']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))


def test_page_login_returning_customer_login_btn_visible(driver, page_login):
    element = (By.XPATH, "//button[@type='submit']")
    WebDriverWait(driver, 3).until(exp.visibility_of_element_located(element))
