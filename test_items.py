
import time
from selenium.webdriver.common.by import By


def test_add_cart_button_present(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    
    cart_button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    
    assert len(cart_button) == 1, 'Add to cart button is not present'
    
    
    
    