#HW7
from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page
class SignInPage(Page):
    SIGN_IN_HEADER = (By.XPATH, '//h1[text()="Sign in or create account"]')# //*[@id="__next"]/div/div/div/div[1]/div/div[2]/div[1]/h1

    def verify_sign_in_form(self):
        assert self.find_element(*self.SIGN_IN_HEADER).is_displayed(), f"Sign In form is not displayed"



# HW8
class TargetSignInPage(Page):
    TTC_LINK = (By.XPATH, '//a[@aria-label="terms & conditions - opens in a new window"]')
    def open_target_term_conditions(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_term_conditions(self):
        self.click(*self.TTC_LINK)
        sleep(3)