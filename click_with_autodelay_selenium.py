from datetime import datetime
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def set_time() -> str:
    """Ввод времени, и проверка на верное форматирование"""
    while True:
        current_time = input()
        if len(current_time.split(':')) == 3 and len(current_time) == 8:  # проверка на формат 00:00:00
            try:
                datetime.strptime(current_time, "%H:%M:%S")
            except:
                print("Неправильно ввёден формат. Введите время в формате '00:00' или '00:00:00' и нажмите Enter:")
                continue
            break
        elif len(current_time.split(':')) == 2 and len(current_time) == 5:  # проверка на формат 00:00
            try:
                datetime.strptime(current_time, "%H:%M")
            except:
                print("Неправильно ввёден формат. Введите время в формате '00:00' или '00:00:00' и нажмите Enter:")
                continue
            break
        else:
            print("Неправильно ввёден формат. Введите время в формате '00:00' или '00:00:00' и нажмите Enter:")
    if len(current_time.split(':')) == 2:  # форматирование 00:00 в 00:00:00
        current_time = current_time + ':00'
    return current_time


def delay() -> str:
    """Проверка задержки времени компьютера через сайт посредством selenium"""
    print('Сейчас будет открыт браузер. Пожалуйста, ничего не трогайте, он закроется автоматически')
    time.sleep(1)
    # Путь до chromedriver. Если что-то не работает - замените chromedriver в папке на версию для Вашего браузера
    driver = webdriver.Chrome(executable_path = 'chromedriver')
    driver.get("https://time100.ru/online")
    try:
        time.sleep(4)
        b = driver.find_element(By.CSS_SELECTOR, 'main>span.time').text.split()
    finally:
        time.sleep(1)
        driver.quit()
        if str(b[4][2:]).isdigit():
            return str(b[4][1:])
        else:
            return '.0'


def time_checker(needed_time: str) -> str:
    """Проверка времени и нажатие кнопки"""
    while True:
        time = datetime.strftime(datetime.now(), "%H:%M:%S.%f")
        if needed_time in str(time):
            pag.click()
            return print(f'Кнопка нажалась в {time}')


print('В какое время нужно кликнуть? Введите в формате "00:00" или "00:00:00" и нажмите Enter:')
actual_time = (set_time() + delay())  # запрос времени и добавление задержки
print(f'Задержка времени на вашем компьютере составляет 0{actual_time[-2:]} секунды')
print('Наведите мышью на нужный элемент, и ждите заданного времени')
time_checker(actual_time)
input('Спасибо за использование программы! Нажмите "Enter", чтобы завершить работу')
