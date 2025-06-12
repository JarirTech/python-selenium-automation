from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# '//div[@class="cell-item-content"]')
@given('Open https://www.target.com/circle')
def circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(1)
@when('verify the page has at least 10 benefit cells')
def verify_benefit(context):
    benefit_cells = context.driver.find_elements(By.XPATH, '//div[@class="cell-item-content"]')
    assert len(benefit_cells) >= 10, f'Error, benefit cells  is less than 10'
    