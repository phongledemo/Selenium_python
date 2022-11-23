from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Locators.locator import Login_locators, Main_locators
from config import username, password
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time




class LinkPage():
    def __init__(self, driver, link_href):
        self.driver = driver
        self.link_href = link_href

    def download_metajson(self):
        for i in self.link_href:
            self.driver.get(i)
            self.driver.implicitly_wait(30)
            try:
                element = WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located(
                        (By.XPATH, Main_locators.metajson_xpath))
                )
                element.click()
                time.sleep(20)
                self.driver.find_element(
                    By.XPATH, Main_locators.button_download_metajson_xpath).click()
            except:
                pass
