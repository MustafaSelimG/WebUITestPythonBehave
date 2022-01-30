from selenium.webdriver.common.by import By


class BasketPage:
    deleteProduct = (By.CSS_SELECTOR, ".js-main-product-delete--basket")
    agreeDelete = (By.CSS_SELECTOR, ".agree-button.btn.btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def deleteTheProduct(self):
        self.driver.find_element(*self.deleteProduct).click()
        self.driver.find_element(*self.agreeDelete).click()