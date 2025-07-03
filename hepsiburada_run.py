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



    clickable_div = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.initialComponent-hk7c_9tvgJ8ELzRuGJwC'))
    )
    driver.execute_script("arguments[0].click();", clickable_div)
    time.sleep(2)

    active_input = WebDriverWait(driver, 20).until(
        lambda d: [el for el in d.find_elements(By.CSS_SELECTOR, "input[class='searchBarContent-UfviL0lUukyp5yKZTi4k']")
                   if el.is_displayed() and el.is_enabled()][-1]
    )

    active_input.send_keys(search_text)
    active_input.send_keys(Keys.ENTER)

    #return []

