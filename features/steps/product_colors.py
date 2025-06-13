from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTION = (By.XPATH, '//li[@class="styles_ndsCarouselItem__dnUkr"]')
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open the A-54475554 product page')
def product_page(context):
    context.driver.get('https://www.target.com/p/men-s-athletic-fit-jeans-goodfellow-co-153/-/A-54475554?preselect=79362266#lnk=sametab')
    sleep(3)

@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Light Blue', 'Black', 'Khaki', 'Light Indigo']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTION)
    for color in colors[:6]:
        actual_colors.append(color.text)
    assert actual_colors == expected_colors, f'Expected colors: {expected_colors}\nActual colors: {actual_colors} are different'