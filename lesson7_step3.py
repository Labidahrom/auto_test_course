from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    x = calc(input_value)
    input_1 = browser.find_element(By.XPATH, "//input[@class='form-control']")
    input_1.send_keys(x)
    robot_click = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robot_click.click()
    robot_rule_click = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robot_rule_click.click()
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла