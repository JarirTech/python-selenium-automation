from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Page:

    def __init__(self, driver, timeout:int=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)



    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    #HW8
    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url), message=f'Expected {partial_url} not in URL')
    def get_current_window_id(self):
        window = self.driver.current_window_handle
        print(f'Original window: {window}')
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f'Switching to a new window: {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window: {window_id}')
        self.driver.switch_to.window(window_id)

    def close_window(self):
        self.driver.close()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, '...'
