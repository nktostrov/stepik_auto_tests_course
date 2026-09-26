from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    robots_radio = browser.find_element(By.ID, "robotsRule") #находим элемент радиобатона robotsRule
    robots_checked = robots_radio.get_attribute("checked") #Найдём атрибут "checked" с помощью встроенного метода get_attribute
    assert robots_checked is None #убедимся, что атрибут отсутствует


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()