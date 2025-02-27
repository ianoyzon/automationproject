import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import logging




driver = webdriver.Chrome()

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.makemytrip.com")

driver.maximize_window()

driver.implicitly_wait(10)


wait = WebDriverWait(driver, 20)

driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[2]/div[2]/div/section").is_displayed()
driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[2]/div[2]/div/section/span").click()
driver.find_element(By.ID, "fromCity").is_displayed()
driver.find_element(By.ID, "fromCity").click()

action = ActionChains(driver)

# driver.find_element(By.NAME, "input").is_displayed()
fromDestination = driver.find_element(By.CLASS_NAME, "react-autosuggest__input")
time.sleep(2)
# fromDestination.click()
fromDestination.send_keys("NYC")
time.sleep(2)
fromDestinationResult = driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']/div/div")
action.move_to_element(fromDestination).click().perform()
fromDestinationResult.click()

driver.find_element(By.ID, "toCity").is_displayed()
driver.find_element(By.ID, "toCity").click()
toDestination = driver.find_element(By.XPATH, "//*[@id='top-banner']/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/input")
toDestination.send_keys("HKG")
time.sleep(2)
toDestinationResult = driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")
action.move_to_element(toDestinationResult).click().perform()
# toDestinationResult.click()
time.sleep(3)


# destinationResult = driver.find_element(By.ID, "react-autowhatever-1-section-0-item-1")
# select = Select(destinationResult)

