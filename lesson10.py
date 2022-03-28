from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    x = browser.find_element_by_id("input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    button_2 = browser.find_element_by_id("solve")
    button_2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()