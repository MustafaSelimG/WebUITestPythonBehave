from selenium.webdriver.common.by import By


class HeaderBanner:
    accountSection = (By.CSS_SELECTOR, ".user-menu__link.user-process-toggle")
    signInButton = (By.CSS_SELECTOR, ".users-process-list__text")
    addressBarClose = (By.CSS_SELECTOR, ".js-subheader-overlay")
    searchBar = (By.CSS_SELECTOR, ".js-illegal-characters")
    searchButton = (By.CSS_SELECTOR, ".btn.product-search__button")

    def __init__(self, driver):
        self.driver = driver

    def closeTheAddressSection(self):
        self.driver.find_element(*self.addressBarClose).click()

    def clickSignIn(self):
        self.driver.find_element(*self.accountSection).click()
        self.driver.find_element(*self.signInButton).click()

    def searchFor(self, searchKey):
        self.driver.find_element(*self.searchBar).send_keys(searchKey)
        self.driver.find_element(*self.searchButton).click()