from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_hepsiburada(search_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.hepsiburada.com")

    try:
        cookie_accept_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_accept_btn.click()
    except:
        print("Çerez kutusu bulunamadı ya da zaten kapalı.")

    time.sleep(1)
    # Arama kutusunu önce bekle, sonra yeniden referans al
    search_input = driver.find_element(By.CSS_SELECTOR, "input[data-test-id='search-bar-input']")
    search_input.click()
    search_input.send_keys(search_text)


    time.sleep(1)
    search_input.send_keys(search_text)
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)

    # Devamında ürünleri çekebilirsin
    time.sleep(3)
    return []