

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-orders%2Forders%3F_encoding%3DUTF8%26ref_%3Dya_d_c_yo&prevRID=A5YDA08FSY3TEPBH8X5C&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_retail_yourorders_us&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_retail_yourorders_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(3)

# Your name
driver.find_element(By.ID, 'ap_customer_name').send_keys('adam')
sleep(3)

#Email
driver.find_element(By.ID, 'ap_email').send_keys('adam@gmail.com')
sleep(3)

# Password
driver.find_element(By.ID, 'ap_password').send_keys('Password')
sleep(3)
# reenter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check').send_keys('Password')
sleep(3)

# create account

driver.find_element(By.CSS_SELECTOR, '#continue').click()
sleep(3)
