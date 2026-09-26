from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value") #находим значение х
    x = x_element.text #задаем значение х - текст между тегами
    y = calc(x)

    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y) #находим поле и вводим туда результат
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click() #находим чек бокс и кликаем на него
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click() #Находим радиобатон и кликаем на него


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()