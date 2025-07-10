from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_amazon(search_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.amazon.com.tr")

    try:
        popup_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                "//button[contains(text(), 'Tamam') or contains(text(), 'Kapat') or contains(text(), 'Devam') or contains(text(), 'Hayır')]"))
        )
        popup_button.click()
        #print("Pop-up butonuna tıklandı.")
    except:
        print("Pop-up çıkmadı veya buton bulunamadı.")

    time.sleep(3)

    try:
        accept_cookies = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
        )
        accept_cookies.click()
        #print("Çerezler kabul edildi.")
    except:
        print("Çerez kutusu görünmedi.")

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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
    )
    time.sleep(2)


    first_product = driver.find_element(By.XPATH, '(//div[@data-component-type="s-search-result"])[1]')
    link = first_product.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.get(link)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )

    results = []
    try:
        name_element = driver.find_element(By.ID, "productTitle")
        name = "Amazon " + name_element.text.strip()


        price_element = driver.execute_script(
            'return document.querySelector(".a-price.a-text-price span.a-offscreen") || document.querySelector("#priceblock_ourprice") || document.querySelector("#priceblock_dealprice") || document.querySelector("#priceblock_saleprice")'
        )
        price = ""
        if price_element:
            price = driver.execute_script("return arguments[0].textContent", price_element).strip()

        if not price:
            price = "Bilinmiyor"

        results.append({"name": name, "price": price})
        #print(f"Ürün: {name}, Fiyat: {price}")
    except Exception as e:
        print(f"Hata: {e}")

    return results
