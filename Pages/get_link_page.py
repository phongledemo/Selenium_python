from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Locators.locator import Login_locators, Main_locators
from config import username, password
from selenium.common.exceptions import NoSuchElementException
import time


class GetLinkPage():

    @staticmethod
    def check_exists_byOptions(driver, option: str, infor: str) -> bool:
        try:
            if option == "ID":
                driver.find_element(By.ID, infor)
            elif option == "NAME":
                driver.find_element(By.NAME, infor)
            elif option == "CSS_SELECTOR":
                driver.find_element(By.CSS_SELECTOR, infor)
            elif option == "CLASS_NAME":
                driver.find_element(By.CLASS_NAME, infor)
            elif option == "TAG_NAME":
                driver.find_element(By.TAG_NAME, infor)
            elif option == "XPATH":
                driver.find_element(By.XPATH, infor)
        except NoSuchElementException:
            return False
        return True

    def __init__(self, driver):
        self.driver = driver
        self.tbody_xpath = Main_locators.tbody_xpath

    def get_link(self):
        try:
            link_href = []
            tbody = driver.find_element(
                By.XPATH, self.tbody_xpath)
            len_tr = len(tbody.find_elements(By.TAG_NAME, 'tr'))
            for i in range(1, len_tr):
                try:
                    table = driver.find_element(
                        By.XPATH, self.tbody_xpath + f'/tr[{i}]/td[14]/a')
                    if "earms-trade.cisco.com" in table.get_attribute("href"):
                        link_href.append(table.get_attribute("href"))
                except:
                    table = driver.find_element(
                        By.XPATH, self.tbody_xpath+f'/tr[{i}]/td[14]')
                    log = table.find_elements(By.TAG_NAME, "p")
                    for i in log:
                        if GetLinkPage.check_exists_byOptions(drivers=i, option="TAG_NAME", infor="a"):
                            elems = i.find_element(By.TAG_NAME, "a")
                            link_href.append(elems.get_attribute("href"))
                    return link_href
        except Exception as e:
            return e
