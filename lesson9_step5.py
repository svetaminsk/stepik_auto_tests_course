from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_window = browser.window_handles[0]
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = browser.find_element_by_id("input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()