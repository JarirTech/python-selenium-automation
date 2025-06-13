from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# '//div[@class="cell-item-content"]')
@given('Open https://www.target.com/circle')
def circle_page(context):
    context.driver.get('https://www.target.com/circle')

@when('verify the page has at least 10 benefit cells')
def verify_benefit(context):
    wait = WebDriverWait(context.driver, 10)
    benefit_cells = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="cell-item-content"]'))
    )
    assert len(benefit_cells) >= 10, f'Error, benefit cells  is less than 10'












