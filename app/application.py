from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage

#HW7
from pages.sign_in_page import SignInPage
from pages.side_nav_menu import SideNavMenu
from pages.product_page import ProductPage
#HW8
from pages.sign_in_page import TargetSignInPage
from pages.ttc_page import TargetTermConditions


class Application:
   def __init__(self, driver):
       self.base_page = Page(driver)
       self.main_page = MainPage(driver)
       self.cart_page = CartPage(driver)
       self.header = Header(driver)
       self.search_results_page = SearchResultsPage(driver)
       #HW7
       self.sign_in_page = SignInPage(driver)
       self.side_nav_menu = SideNavMenu(driver)
       #HW7#2
       self.product_page = ProductPage(driver)
       #HW8
       self.target_sign_in_page = TargetSignInPage(driver)
       self.ttc_page = TargetTermConditions(driver)


