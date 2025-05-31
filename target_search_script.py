#2. Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)
#
# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
# 2. Click Account button
# 3. Click SignIn btn from side navigation
# 4. Verify SignIn page opened:
# “Sign in or create account” text is shown,
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open https://www.target.com/
browser = webdriver.Chrome()
browser.get('https://www.target.com/')
sleep(3)

# 2. Click Account button
browser.find_element(By.XPATH, '//span[@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]').click()
sleep(3)

#3. Click SignIn btn from side navigation

browser.find_element(By.XPATH, "//*[text()='Sign in or create account']").click()
sleep(3)


#4. Verify SignIn page opened:
#Sign in or create account text is shown,
#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

expected_result = "Sign in or create account"

actual_result = browser.find_element(By.XPATH, "//*[text()='Sign in or create account']").text


assert expected_result in actual_result, f'error,expected {expected_result} not in actual {actual_result}'
print('Test passed')





