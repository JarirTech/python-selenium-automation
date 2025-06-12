from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('click on shopping cart icon')
def shopping_cart(context):
    context.driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/a[5]').click()
    sleep(3)

@then('shopping cart is empty')
def verify_cart(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.XPATH, '//*[@id="cart-container"]/div[1]/div/div/div[2]/h1').text
    assert expected_result in actual_result, f"Error {expected_result} is not in {actual_result}"
