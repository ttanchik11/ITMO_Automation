#  задачка 1

from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
if username is None:
    print('Поле логина не найден')
else:
    print("Поле логина найден")

password = driver.find_element(By.CSS_SELECTOR, '#password')
if password is None:
    print('Поле пароля не найден')
else:
    print("Поле пароля найден")

submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
if submit is None:
    print('Кнопка не найдена')
else:
    print("Кнопка найден")

driver.quit()
