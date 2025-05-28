from webbrowser import Chrome

from requests import options
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


service = ChromeService("./chromedriver.exe")

driver.get("http://apple.com")
