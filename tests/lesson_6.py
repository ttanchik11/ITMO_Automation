from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img1')
if icon is None:
    print('Элемент не найден')
else:
    print("Элемент найден")
driver.quit()