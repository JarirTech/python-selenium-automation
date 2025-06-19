#HW7
from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    FIRST_ADD_TO_CART_BTN = (By.XPATH, '(//button[contains(@id,"addToCartButtonOrTextIdFor")])[1]')
    CONFIRM_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="content-wrapper"] button[id*="addToCartButton"]')

    def click_add_to_cart(self):
        self.click(*self.FIRST_ADD_TO_CART_BTN)

    def confirm_add_to_cart_sidebar(self):
        self.click(*self.CONFIRM_ADD_TO_CART_BTN)

    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')
