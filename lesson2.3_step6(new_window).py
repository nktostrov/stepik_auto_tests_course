from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "trollface") #находим и нажимаем на кнопку 
    button1.click()   
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(3)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y) #находим поле и вводим туда результат
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()