import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support import ui


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def verifyHomepage(self):
        wait = ui.WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be("https://www.ciceksepeti.com/"))