from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HELP_URL = "https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges"

@given("open the Target help page")
def open_help(context):
    context.driver.get(HELP_URL)

@when('choose "{topic}" from the topic dropdown')
def choose_topic(context, topic):
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//select[@id="j_id0:contentTemplate:j_id79:j_id80:viewHelpTopics:ViewHelpTopics"]'))
    )
    Select(dropdown).select_by_visible_text("Gift Cards")

@when('click the "{topic}" button')
def click_topic_button(context, topic):
    context.driver.find_element(By.XPATH, '//option[@value="Gift Cards"]').click()

@then('the URL contains "{slug}"')
def step_verify_url(context, slug):
    WebDriverWait(context.driver, 10).until(EC.url_contains(slug))
    assert slug in context.driver.current_url