from core.healed_driver import HealedDriver
from pages.login_page import LoginPage

def test_login():
    driver = HealedDriver()

    driver.get("https://the-internet.herokuapp.com/login")

    page = LoginPage(driver)

    page.enter_username("admin")
    page.enter_password("123456")

    driver.quit()