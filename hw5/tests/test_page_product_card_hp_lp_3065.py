from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_hp_lp_3065_title_visible(driver, click_laptop):
    hp_lp_3065_page = driver.find_element(By.XPATH, '//div[@id="product-list"]/div[1]/div/div[1]/a/img')
    hp_lp_3065_page.click()
    assert driver.current_url == "http://localhost/en-gb/product/laptop-notebook/hp-lp3065"
    driver.back()


def test_page_hp_lp_3065_title_text_in_script(driver, click_laptop):
    hp_lp_3065_page = driver.find_element(By.XPATH, '//div[@id="product-list"]/div[1]/div/div[1]/a/img')
    hp_lp_3065_page.click()
    xpath = (By.TAG_NAME, 'h1')
    title = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element(xpath, "HP LP3065"))
    assert title.text == "HP LP3065"
    driver.back()


def test_page_hp_lp_3065_price_visible(driver, click_laptop):
    hp_lp_3065_page = driver.find_element(By.XPATH, '//div[@id="product-list"]/div[1]/div/div[1]/a/img')
    hp_lp_3065_page.click()
    xpath = (By.XPATH, "//span[@class='price-new']")
    price = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert price.is_displayed()
    driver.back()


def test_page_hp_lp_3065_add_to_card_btn_visible(driver, click_laptop):
    hp_lp_3065_page = driver.find_element(By.XPATH, '//div[@id="product-list"]/div[1]/div/div[1]/a/img')
    hp_lp_3065_page.click()
    xpath = (By.XPATH, "//button[@id='button-cart']")
    add_to_card_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(xpath))
    assert add_to_card_btn.is_displayed()
    driver.back()


def test_page_hp_lp_3065_add_to_card_btn_clickable(driver, click_laptop):
    hp_lp_3065_page = driver.find_element(By.XPATH, '//div[@id="product-list"]/div[1]/div/div[1]/a/img')
    hp_lp_3065_page.click()
    xpath = (By.XPATH, "//button[@id='button-cart']")
    add_to_card_btn = driver.find_element(*xpath)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(xpath))
    assert add_to_card_btn.is_enabled()
    driver.back()
