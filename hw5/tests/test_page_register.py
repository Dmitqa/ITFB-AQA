from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_register_title_visible(driver, page_register):
    xpath = (By.TAG_NAME, "h1")
    title = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert title.is_displayed()


def test_page_register_title_text_in_script(driver, page_register):
    xpath = (By.TAG_NAME, "h1")
    title = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element(xpath, "Register Account"))
    assert title.text == "Register Account"


def test_page_register_modal_window_visible(driver, page_register):
    xpath = (By.XPATH, "//div[@id='content']")
    window = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located(xpath))
    assert window.is_displayed()


def test_page_register_field_name_visible(driver, page_register):
    xpath = (By.XPATH, '//fieldset[@id="account"]/div[1]/label')
    field_name = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert field_name.text == "First Name"


def test_page_register_privacy_policy_check_box_visible(driver, page_register):
    xpath = (By.XPATH, "//input[@type='checkbox' and @name='agree']")
    box = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert not box.is_selected()
