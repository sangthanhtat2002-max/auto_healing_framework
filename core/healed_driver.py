from selenium import webdriver
from selenium.webdriver.common.by import By
from core.healer import Healer

class HealedDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.healer = Healer(self.driver)

    def get(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        try:
            return self.driver.find_element(by, value)

        except Exception as e:
            print(f"[WRAPPER] Element not found: {by}={value}")
            return self.healer.heal(by, value)

    def quit(self):
        self.driver.quit()