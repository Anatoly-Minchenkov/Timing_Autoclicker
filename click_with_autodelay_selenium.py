from datetime import datetime
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def delay() -> str:
    """Смотрит задержку времени на сатйе и возвращает её"""
    driver = webdriver.Chrome()
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


print('В какое время нужно кликнуть? Напишите в формате "00:00" или "00:00:00" и нажмите Enter:')

while True:

    curretn_time = input()
    if len(curretn_time.split(':')) == 3:
        try:
            datetime.strptime(curretn_time, "%H:%M:%S")
        except:
            print("Неправильно ввёден формат. Введите время в формате '00:00' или '00:00:00' и нажмите Enter:")
            continue
        break
    else:
        try:
            datetime.strptime(curretn_time, "%H:%M")
        except:
            print("Неправильно ввёден формат. Введите время в формате '00:00' или '00:00:00' и нажмите Enter:")
            continue
        break

if len(curretn_time.split(':')) == 2:
    curretn_time = (curretn_time + ':00')
curretn_time = (curretn_time + delay())  # задержка милисекунду
print(f'Задержка равна 0{curretn_time[-2:]} секунды')

print('Наведите мышью на нужный элемент, и ждите заданного времени')
while True:
    time = datetime.strftime(datetime.now(), "%H:%M:%S.%f")

    if curretn_time in str(time):
        pag.click()
        print(f'Кнопка нажалась в {time}')
        break
input('Нажмите "Enter", чтобы закрыть программу')
