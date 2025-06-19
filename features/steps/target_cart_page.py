from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@when('click on Add to Cart button')
def add_to_cart(context):
    # HW7
    # wait = WebDriverWait(context.driver, 10)
    # add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addToCartButtonOrTextIdFor77334539"]')))
    # add_button.click()

    context.app.product_page.click_add_to_cart()
    sleep(3)




@when('confirm Add to Cart button from side bar')
def confirm_add_to_cart(context):
    wait = WebDriverWait(context.driver, 10)
    #HW7
    # confirm_button = wait.until(
    # EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="content-wrapper"] button[id*="addToCartButton"]')))
    # confirm_button.click()
    context.app.product_page.confirm_add_to_cart_sidebar()


@when('open cart page')
def open_cart_page(context):
    #HW7

    # context.driver.get('https://www.target.com/cart')
    # sleep(3)
    context.app.product_page.open_cart_page()
    sleep(3)


@then('Verify cart has {amount} item')
def verify_cart(context, amount):
    wait = WebDriverWait(context.driver, 10)
    cart_text = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="sc-46253dd2-2 ijhCkR"]'))).text
    assert f'{amount} item' in cart_text, f"Expected {amount} item but got {cart_text}"


    # actual_cart= context.driver.find_element(By.XPATH, '//span[@class="sc-46253dd2-2 ijhCkR"]').text
    # assert f'{amount} item' in actual_cart, f"expected {amount} item but got  {actual_cart} item"

