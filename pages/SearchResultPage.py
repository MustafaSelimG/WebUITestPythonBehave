from selenium.webdriver.common.by import By


class SearchResultPage:
    colorFilter = (By.CSS_SELECTOR, ".js-filter-item:nth-child(5)")
    colorSearch = (By.XPATH, "(//input[@class='filter__dropdown-input js-category-filter-input js-only-alphanumeric-characters'])[5]")
    colorList = (By.XPATH, "//li[@class='filter__dropdown-list js-filter-dropdown-list']")
    product = (By.CSS_SELECTOR,".ad-product--1.js-ad-product--p1")

    def __init__(self, driver):
        self.driver = driver

    def filterColor(self, color):
        self.driver.find_element(*self.colorFilter).click()
        self.driver.find_element(*self.colorSearch).send_keys(color)
        self.driver.find_element(*self.colorList).click()
        self.driver.find_element(*self.colorFilter).click()

    def selectTheProduct(self):
        self.driver.find_element(*self.product).click()