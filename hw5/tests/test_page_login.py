from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp


def test_page_login_modal_window_new_customer_visible(driver, page_login):
    xpath = (By.XPATH, "//div[@id='content']/div/div[1]/div")
    window_new_customer = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert window_new_customer.is_displayed()


def test_page_login_modal_window_new_customer_title_text_in_script(driver, page_login):
    xpath = (By.TAG_NAME, "h2")
    window_new_customer = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.text_to_be_present_in_element(
        xpath, "New Customer"))
    assert window_new_customer.text == "New Customer"


def test_page_login_new_customer_continue_button_visible(driver, page_login):
    xpath = (By.XPATH, "//a[contains(text(), 'Continue')]")
    continue_button = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert continue_button.is_displayed()


def test_page_login_returning_customer_email_field_visible(driver, page_login):
    xpath = (By.XPATH, "//input[@id='input-email']")
    customer_email_field = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert customer_email_field.is_displayed()


def test_page_login_returning_customer_email_in_field(driver, page_login):
    xpath = (By.XPATH, "//input[@id='input-email']")
    customer_email_field = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(exp.visibility_of_element_located(xpath))
    assert customer_email_field.get_attribute("placeholder") == "E-Mail Address"
