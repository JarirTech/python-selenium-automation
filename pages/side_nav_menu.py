#HW7
from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideNavMenu(Page):
    SIGN_IN_LINK = (By.XPATH, "//*[text()='Sign in or create account']")

    def click_sign_in_from_menu(self):
        self.click(*self.SIGN_IN_LINK)