import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_chech_add_book_to_basket (browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        add_to_basket_button = WebDriverWait(browser, 10).until(
         EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_basket_form"]/button')))
        assert add_to_basket_button.is_displayed()
    except:
        pytest.fail("Can't find button Add to basket")


