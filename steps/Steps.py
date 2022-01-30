from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.HomePage import HomePage
from pages.HeaderBanner import HeaderBanner
from pages.SearchResultPage import SearchResultPage
from pages.ProductPage import ProductPage
from pages.BasketPage import BasketPage
from pages.SignInPage import SignInPage


class Steps(HomePage, HeaderBanner, SearchResultPage, ProductPage, BasketPage, SignInPage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @given('navigate to website')
    def navigateToWebsite(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ciceksepeti.com/")

    @step("close the address selection")
    def close_the_address(self):
        HeaderBanner(self.driver).closeTheAddressSection()

    @when("open sign in page")
    def open_sign_in_page(self):
        HeaderBanner(self.driver).clickSignIn()

    @step('enter email "{email}" and password "{password}"')
    def enter_email_and_password(self, email, password):
        SignInPage(self.driver).SignIn(email, password)

    @then('verify homepage is open')
    def verify_homepage_is_open(self):
        HomePage(self.driver).verifyHomepage()

    @when('search for "{searchKey}"')
    def search_for(self, searchKey):
        HeaderBanner(self.driver).searchFor(searchKey)

    @step('filter "{color}" color ones')
    def filter_color_ones(self, color):
        SearchResultPage(self.driver).filterColor(color)

    @step("select the first product")
    def select_the_first_product(self):
        SearchResultPage(self.driver).selectTheProduct()

    @step("add product to basket")
    def add_product_to_basket(self):
        ProductPage(self.driver).addBasket()

    @step("delete product from the basket")
    def delete_product_from_the_basket(self):
        BasketPage(self.driver).deleteTheProduct()
