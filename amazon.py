from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_amazon(search_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.amazon.com.tr")

    try:
        accept_cookies = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
        )
        accept_cookies.click()
        print("Çerezler kabul edildi.")
    except:
        print("Çerez kutusu görünmedi.")

    time.sleep(2)

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(search_text)
    search_box.send_keys(Keys.ENTER)

    try:
        sort_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "s-result-sort-select"))
        )
        Select(sort_dropdown).select_by_value("price-asc-rank")
    except Exception as e:
        print("Sıralama kutusu bulunamadı:", e)

    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
    )
    results = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

    first_product = results[0]



    try:
        name = "Amazon " + first_product.find_element(By.XPATH, './/h2').get_attribute("aria-label")
        price = first_product.find_element(By.CSS_SELECTOR, "span.a-price > span.a-offscreen").text
        print(f"Ürün: {name}, Fiyat: {price}")
    except Exception as e:
        print(f"Hata: {e}")

    print(results)
    return results




