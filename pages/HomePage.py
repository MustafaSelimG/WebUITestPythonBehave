import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support import ui


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def verifyHomepage(self):
        wait = ui.WebDriverWait(self.driver, 20)
        wait.until(EC.url_to_be("https://www.ciceksepeti.com/"))
        # current_url = self.driver.current_url
        # assert(current_url,"https://www.ciceksepeti.com")