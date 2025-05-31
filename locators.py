#HW2
# 1. Practice with locators.
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# create instance of the object driver

driver = webdriver.Chrome()
driver.maximize_window()
#
# # get the url
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
sleep(3)
#
# # locators
# # logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]').click()


# email
driver.find_element(By.XPATH, "//input[@id ='ap_email']").click()

#continue

driver.find_element(By.XPATH, "//span[@class='a-button a-button-span12 a-button-primary']").click()

#Conditions of use link
driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[1]").click()

# Privacy Notice link
driver.find_element(By.XPATH, '//*[@id="legalTextRow"]/a[2]').click()

# Need help
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').click()


#Forgot your password link
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').click()
sleep(2)
driver.find_element(By.ID, "auth-fpp-link-bottom").click()
sleep(5)

# Other issues with Sign-In link
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="ap-other-signin-issues-link"]').click()

#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit").click()



