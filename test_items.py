from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_chech_add_book_to_basket (browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_busket_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_basket_form"]/button'))
    )
    assert
    if language=="ru":
        assert 'Добавить в корзину'==add_to_busket_button.text, \
        f'{add_to_busket_button.text} is not Добавить в корзину'

    if language=="es":
        assert 'Añadir al carrito'==add_to_busket_button.text, \
        f'{add_to_busket_button.text} is not Añadir al carrito'

    if language=="en - gb":
        assert 'Add to basket'==add_to_busket_button.text, \
        f'{add_to_busket_button.text} is not Add to basket'

