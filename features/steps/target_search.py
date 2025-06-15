from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('search for {search_word}')

def search_product(context, search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(10)
    context.app.header.search_product()


@then('verify that search for {product} worked')
def verify_search_worked(context, product):
   # actual_result = context.driver.find_element(By.XPATH, '//span[@class="h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2"]').text
   # assert productName in actual_result, f'Error, expected {productName} is not in {actual_result}'

   context.app.search_results_page.verify_search_results()

