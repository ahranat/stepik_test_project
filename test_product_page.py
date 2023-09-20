import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()


if __name__ == '__main__':
    pytest.main()