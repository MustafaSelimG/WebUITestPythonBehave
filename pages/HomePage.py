from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    homepageContainer = (By.CSS_SELECTOR, ".hl-full-bleed-banner__image-container")

    def clickSignIn(self):
        pass