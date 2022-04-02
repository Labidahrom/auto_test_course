from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name_input = browser.find_element(By.XPATH, "//input[@name = 'firstname']")
    name_input.send_keys("Хай")
    surname_input = browser.find_element(By.XPATH, "//input[@name = 'lastname']")
    surname_input.send_keys("Хай")
    email_input = browser.find_element(By.XPATH, "//input[@name = 'email']")
    email_input.send_keys("Хай")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input = browser.find_element(By.XPATH, "//input[@name = 'file']")
    file_input.send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button[@class = 'btn btn-primary']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

