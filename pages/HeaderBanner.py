from selenium.webdriver.common.by import By


class HeaderBanner:
    def __init__(self, driver):
        self.driver = driver

    shopByCategoryButton = (By.ID, "gh-shop-a")
    guitarCategory = (By.XPATH, "//a[@_sp='m570.l6384']")
    searchBar = (By.ID, "gh-ac")
    signInButton = (By.XPATH, "//a[@_sp='m570.l1524']")
    username = (By.XPATH, "//*[@id='gh-ug']/b[1]")
