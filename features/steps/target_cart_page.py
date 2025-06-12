from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from target_search_script import actual_result


@when('click on Add to Cart button')
def add_to_cart(context):
    context.driver.find_element(By.XPATH, '//*[@id="addToCartButtonOrTextIdFor77334539"]').click()
    sleep(3)
@when('confirm Add to Cart button from side bar')
def confirm_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="content-wrapper"] button[id*="addToCartButton"]').click()
    sleep(3)
@when('open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')
    sleep(3)

@then('Verify cart has {amount} item')
def verify_cart(context, amount):
    actual_cart= context.driver.find_element(By.XPATH, '//span[@class="sc-46253dd2-2 ijhCkR"]').text
    assert f'{amount} item' in actual_cart, f"expected {amount} item but got  {actual_cart} item"

