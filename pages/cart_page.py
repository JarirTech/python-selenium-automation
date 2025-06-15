from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    cart_empty_txt = 'Your cart is empty'
    # Locators
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        self.verify_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)

