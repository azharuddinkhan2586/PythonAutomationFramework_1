from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import contantUtils as config
from utils import utils as utils
@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(config.URL)
        login = LoginPage(driver)
        login.enter_username(config.USERNAME)
        login.enter_password(config.PASSWORD)
        login.click_loginButton()
        print("Login Test Cases Completed.....")

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion Error as Occrured")
            print(error)
            utils.capturescreenshot(self.driver, utils.currenttestname())
            raise

        except:
            print("Some exception occurred")
            utils.capturescreenshot(self.driver, utils.currenttestname())
        else:
            print("No Exception Occured")
        finally:
            print("I am inside finally Block")