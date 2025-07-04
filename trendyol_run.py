from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def search_trendyol(search_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.trendyol.com")


    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))
        )
        close_button.click()
    except:
        pass


    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='suggestion']"))
    )
    search_input.send_keys(search_text)

    search_icon = driver.find_element(By.CSS_SELECTOR, "i[data-testid='search-icon']")
    search_icon.click()


    dropdown_menu = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "search-sort-container"))
    )
    dropdown_menu.click()

    lowest_price_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='En düşük fiyat']"))
    )
    lowest_price_option.click()


    WebDriverWait(driver, 15).until(
        EC.staleness_of(driver.find_element(By.CLASS_NAME, "p-card-wrppr"))
    )


    first_product = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "p-card-wrppr"))
    )[0]

    results = []
    try:
        name = "Trendyol " + first_product.find_element(By.CLASS_NAME, 'prdct-desc-cntnr').text
        try:
            price = first_product.find_element(By.CLASS_NAME, 'prc-box-dscntd').text
        except:
            price = first_product.find_element(By.CLASS_NAME, 'price-information').text
        results.append({"name": name, "price": price})
    except:
        pass

    # driver.quit()
    return results
