from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[@class = 'trollface btn btn-primary']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = calc(browser.find_element(By.XPATH, "//span[@id = 'input_value']").text)
    print(x)
    browser.find_element(By.XPATH, "//input[@id = 'answer']").send_keys(x)
    button1 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд, и просто 1 изменение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

