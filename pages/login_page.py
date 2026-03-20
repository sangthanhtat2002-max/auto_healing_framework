from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    # 🔥 phải inspect lại nếu sai
    LOGIN_OUTSIDE_BTN = (By.XPATH, "//button[normalize-space()='Login']")

    USERNAME = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def open_login_form(self):
        WebDriverWait(self.driver.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_OUTSIDE_BTN)
        ).click()

    def enter_username(self, username):
        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BTN)
        ).click()

    # 🔥 full flow
    def login(self, username, password):
        self.open_login_form()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()