from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

time.sleep(5)

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img1')
if icon is None:
    print('Элемент не найден')
else:
    print("Элемент найден")
input("Нажмите Enter чтобы закрыть браузер...")  # Браузер останется открытым
driver.quit()
