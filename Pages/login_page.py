from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Locators.locator import Login_locators, Main_locators
from config import username, password
import time


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.userInput_id = Login_locators.userInput_id
        self.passwordInput_id = Login_locators.passwordInput_id
        self.login_button_id = Login_locators.login_button_id
        self.trust_brower_button_id = Login_locators.trust_brower_button_id
        self.tbody_xpath = Login_locators.tbody_xpath

    def type_user_and_login(self):
        try:
            self.driver.find_element(By.ID, self.userInput_id).send_keys(username)
            self.driver.find_element(By.ID, self.login_button_xpath).click()
            time.sleep(10)
            self.driver.find_element(
                By.ID, self.passwordInput_id).send_keys(password)
            self.driver.find_element(By.ID, self.login_button_id).click()
            time.sleep(20)
            # if check_exists_byOptions(drivers = driver, option="ID", infor='trust-browser-button'):
            self.driver.find_element(By.ID, self.trust_brower_button_id).click()
            time.sleep(30)
        except Exception as e:
            return e