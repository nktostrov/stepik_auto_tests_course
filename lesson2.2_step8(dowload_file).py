from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

  
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("IVAN") #находим поле и вводим туда результат
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("IVANOV")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("IVANOV@MAIL.RU")
    file_path1 = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'Text Document.txt')           # добавляем к этому пути имя файла 
    file_path1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()