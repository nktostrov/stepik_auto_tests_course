from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    people_radio = browser.find_element(By.ID, "peopleRule") #находим элемент радиобатона People rule
    people_checked = people_radio.get_attribute("checked") #Найдём атрибут "checked" с помощью встроенного метода get_attribute
    print("value of people radio: ", people_checked) #выведем текст и значение атрибута, которое получили
    assert people_checked is not None, "People radio is not selected by default" #Я утверждаю, что переменная people_checked НЕ равна None, либо выводится ошибка People radio is not selected by default


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()