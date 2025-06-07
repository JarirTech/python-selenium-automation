from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('click on account button')
def account_button(context):
    context.driver.find_element(By.XPATH, '//span[@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]').click()
    sleep(3)
@then('Click SignIn button from side navigation')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").click()
sleep(3)

@then('Verify SignIn page opened')
def verify_signin(context):
    expected_result = "Sign in or create account"

    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text

    assert expected_result in actual_result, f'error,expected {expected_result} not in actual {actual_result}'
    sleep(3)
