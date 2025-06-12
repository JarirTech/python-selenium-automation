from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('search for {productName}')
def search_product(context, productName):
    context.driver.find_element(By.XPATH, '//input[@aria-label="What can we help you find? suggestions appear below"]').send_keys(productName)
    sleep(1)
    context.driver.find_element(By.XPATH, '//button[@aria-label="search"]').click()
    sleep(3)


@then('verify that search for {productName} worked')
def verify_search_worked(context, productName):
    actual_result = context.driver.find_element(By.XPATH, '//span[@class="h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2"]').text
    assert productName in actual_result, f'Error, expected {productName} is not in {actual_result}'