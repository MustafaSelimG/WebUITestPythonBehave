from selenium.webdriver.common.by import By


class SignInPage:
    emailBar = (By.CSS_SELECTOR, ".js-placeholder")
    passwordBar = (By.CSS_SELECTOR, ".js-html-tag-replace")
    signInButton = (By.CSS_SELECTOR, ".js-login-button")

    def __init__(self, driver):
        self.driver = driver

    def SignIn(self, email, password):
        self.driver.find_element(*self.emailBar).send_keys(email)
        self.driver.find_element(*self.passwordBar).send_keys(password)
        self.driver.find_element(*self.signInButton).click()
