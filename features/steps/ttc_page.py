
from selenium.webdriver.common.by import By
from time import sleep

from behave import given, when, then
from pages.base_page import Page


@given('Open sign in page')
def open_target_term_conditions(context):
    context.app.target_sign_in_page.open_target_term_conditions()
    sleep(3)



@when('Store original window')
def store_window(context):
    context.original_window = context.app.target_sign_in_page.get_current_window_id()



@when('Click on Target terms and conditions link')
def click_ttc_link(context):
    context.app.target_sign_in_page.click_term_conditions()



@when('Switch to the newly opened window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_ttc_opened(context):
    context.app.ttc_page.verify_ttc_opened()


@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close_window()


def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)