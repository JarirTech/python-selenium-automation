#HW7
from selenium.webdriver.common.by import By
from pages.base_page import Page
class SignInPage(Page):
    SIGN_IN_HEADER = (By.XPATH, '//h1[text()="Sign in or create account"]')# //*[@id="__next"]/div/div/div/div[1]/div/div[2]/div[1]/h1

    def verify_sign_in_form(self):
        assert self.find_element(*self.SIGN_IN_HEADER).is_displayed(), f"Sign In form is not displayed"
        