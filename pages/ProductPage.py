from selenium.webdriver.common.by import By


class ProductPage:
    addBasketButton = (By.CSS_SELECTOR, ".js-product-datas.js-clickable-by-tab")

    def __init__(self, driver):
        self.driver = driver

    def addBasket(self):
        self.driver.find_element(*self.addBasketButton).click()