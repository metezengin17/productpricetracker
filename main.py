import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webbrowser import Chrome

from requests import options
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


service = ChromeService("./chromedriver.exe")
driver.maximize_window()
driver.get("http://trendyol.com")

trenydol_close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))
)
trenydol_close_button.click()

trenydol_input_element = driver.find_element(By.CSS_SELECTOR, "input[data-testid='suggestion']")
trenydol_input_element.send_keys("champion tshirt")

trenydol_search_element = driver.find_element(By.CSS_SELECTOR, "i[data-testid='search-icon']")
trenydol_search_element.click()

last_height = driver.execute_script("return document.body.scrollHeight")

import time

scroll_pause_time = 1  # scrolllar arası bekleme süresi
scroll_amount = 500    # her seferinde kaç px kaydırılacak


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "prdct-cntnr-wrppr"))
)

