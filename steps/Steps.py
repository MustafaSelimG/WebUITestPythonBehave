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
        super().__init__(driver)


    @given('navigate to website')
    def navigateToWebsite(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")


    @step("open sign in page")
    def open_sign_in_page(self):
        HomePage(self.driver).clickSignIn()


    @then("verify sign in")
    def verify_sign_in(self):



    @when("open shop by category")
    def open_shop_by_category(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: When open shop by category')


    @step("select guitar")
    def select_guitar(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And select guitar')


    @step("randomly select a submenu")
    def randomly_select_a_submenu(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And randomly select a submenu')


    @step("randomly select a product")
    def randomly_select_a_product(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And randomly select a product')


    @step("open the product in new tab")
    def open_the_product_in_new_tab(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And open the product in new tab')


    @step("add product the cart")
    def add_product_the_cart(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And add product the cart')


    @step("close the tab")
    def close_the_tab(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And close the tab')


    @step("open the basket")
    def open_the_basket(self):
        """
        :type context: behave.runner.Context
        """
        raise NotImplementedError(u'STEP: And open the basket')


    @then("product should be seen in the basket")
    def product_should_be_seen_in_the_basket(self):
        raise NotImplementedError(u'STEP: Then product should be seen in the basket')
