from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_trendyol(search_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://trendyol.com")

    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))
        )
        close_button.click()
    except:
        pass

    search_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='suggestion']")
    search_input.send_keys(search_text)

    search_icon = driver.find_element(By.CSS_SELECTOR, "i[data-testid='search-icon']")
    search_icon.click()

    # Burada filtreleme, sıralama vs işlemler olabilir
    time.sleep(2)  # örnek bekleme

    # Ürünleri çekip dönebilirsin
    products_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div'))
    )
    product_cards = products_container.find_elements(By.CLASS_NAME, 'p-card-wrppr')

    results = []
    for product in product_cards[:5]:  # İlk 5 ürünü örnek alalım
        try:
            name = product.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
            try:
                price = product.find_element(By.CSS_SELECTOR, 'div.basket-price-original-wrapper > div.price-item.basket-price-original').text
            except:
                price = product.find_element(By.CLASS_NAME, 'price-information').text
            results.append({"name": name, "price": price})
        except:
            continue

    #driver.quit()
    return results

