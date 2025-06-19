
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    #HW7
    ACCOUNT_BTN = (By.XPATH, '//span[@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]')

    def search_product(self):
        self.input_text('toys', *self.SEARCH_FIELD)
        sleep(1)
        self.click(*self.SEARCH_BTN)
        sleep(10)
    # HW7
    def click_sign_in(self):
        self.click(*self.ACCOUNT_BTN)
