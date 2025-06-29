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
trenydol_input_element.send_keys("Apple iphone 16 1tb")

trenydol_search_element = driver.find_element(By.CSS_SELECTOR, "i[data-testid='search-icon']")
trenydol_search_element.click()


filter_dropdown = driver.find_element(By.XPATH, '//*[@id="search-app"]/div/div/div/div[2]/div[1]/div[2]/div/div')
filter_dropdown.click()

lowest_price_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="search-app"]/div/div/div/div[2]/div[1]/div[2]/div/ul/li[2]'))
)
lowest_price_option.click()
time.sleep(1)

products_container = driver.find_element(By.XPATH, '//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div')
product_cards = products_container.find_elements(By.CLASS_NAME, 'p-card-wrppr')


first_product = product_cards[0]  # En düşük fiyatlı ürün
product_name = first_product.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
try:
    product_price = first_product.find_element(By.CSS_SELECTOR, 'div.basket-price-original-wrapper > div.price-item.basket-price-original').text
except:
    product_price = first_product.find_element(By.CLASS_NAME, 'price-information').text

print(f"En ucuz ürün: {product_name}")
print(f"Fiyatı: {product_price}")







