from core.healed_driver import HealedDriver
from pages.login_page import LoginPage


def test_login():
    driver = HealedDriver()

    driver.get("")

    page = LoginPage(driver)

    page.login("admin", "123456")

    driver.quit()
