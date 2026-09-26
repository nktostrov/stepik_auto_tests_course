from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.get(link)
    button1 = browser.find_element(By.ID, "book") #находим кнопку 
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100")) #ждем когда цена упадет до 100
    button1.click() # и жмём кнопку
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y) #находим поле и вводим туда результат
    
    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()