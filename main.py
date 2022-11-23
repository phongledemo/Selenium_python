from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
# trust-brower-button
DNAC_Shockwave_Solution = "https://wiki.cisco.com/display/EDPEIXOT/DNAC+Shockwave+Solution+Sanity+Reports"

driver.get(
    "https://wiki.cisco.com/display/EDPEIXOT/DNAC+Shockwave+Solution+Sanity+Reports")


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


def Login_and_Authenticate(driver) -> bool:
    try:
        driver.find_element(By.ID, 'userInput').send_keys("phonghle@cisco.com")
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(10)
        driver.find_element(
            By.ID, 'passwordInput').send_keys("WindyLe78201330@")
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(30)
        # if check_exists_byOptions(drivers = driver, option="ID", infor='trust-browser-button'):
        driver.find_element(By.ID, 'trust-browser-button').click()
        time.sleep(60)
        return True
    except Exception as e:
        return False

# LOGIN


def DNAC_Shockwave():
    try:
        link_href = []
        if Login_and_Authenticate(driver):
            tbody = driver.find_element(
                By.XPATH, '//*[@id="main-content"]/div[2]/table/tbody')
            len_tr = len(tbody.find_elements(By.TAG_NAME, 'tr'))
            for i in range(1, len_tr):
                try:
                    table = driver.find_element(
                        By.XPATH, f'//*[@id="main-content"]/div[2]/table/tbody/tr[{i}]/td[14]/a')
                    if "earms-trade.cisco.com" in table.get_attribute("href"):
                        link_href.append(table.get_attribute("href"))
                except:
                    table = driver.find_element(
                        By.XPATH, f'//*[@id="main-content"]/div[2]/table/tbody/tr[{i}]/td[14]')
                    log = table.find_elements(By.TAG_NAME, "p")
                    for i in log:
                        if check_exists_byOptions(drivers=i, option="TAG_NAME", infor="a"):
                            elems = i.find_element(By.TAG_NAME, "a")
                            link_href.append(elems.get_attribute("href"))
            return link_href
    except:
        return "Error"
    # finally:
    #     driver.quit()


link_href = DNAC_Shockwave()

for i in link_href:
    driver.get(i)
    driver.implicitly_wait(30)
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[text() = 'meta.json']"))
        )
        element.click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    except:
        pass
