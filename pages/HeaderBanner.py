from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HeaderBanner:
    accountSection = (By.CSS_SELECTOR, ".user-menu__link.user-process-toggle")
    signInButton = (By.CSS_SELECTOR, ".users-process-list__text")
    addressBarClose = (By.CSS_SELECTOR, ".js-subheader-overlay")

    searchBar = (By.CSS_SELECTOR, ".js-illegal-characters")

    def __init__(self, driver):
        self.driver = driver

    def closeTheAddressSection(self):
        self.driver.find_element(*self.addressBarClose).click()

    def clickSignIn(self):
        self.driver.find_element(*self.accountSection).click()
        self.driver.find_element(*self.signInButton).click()

