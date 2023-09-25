import pytest 
from .pages.product_page import ProductPage
from .pages.bascket_page import BasketPage



links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Won't fix")),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        ]
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

class TestNegative:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_disappear_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, self.link)
        page.open()
        page.go_to_main_page()
        page.go_to_basket()
        page.should_not_be_basket_items()
        page.should_be_empty_basket_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(browser, self.link)
        page.open()
        page.go_to_basket()
        page.should_not_be_basket_items()
        page.should_be_empty_basket_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    def test_user_cant_see_success_message(self, browser, create_new_user):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, create_new_user):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


if __name__ == '__main__':
    pytest.main()