"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep as wait
from datetime import datetime as d_t

class TrafficLight:
    colors = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    color = ''

    def burn(pers):
        for color, sw_time in pers.colors.items():
            pers.color = color
            start_state_time = d_t.now()

            print(f"Светофор горит цветом '{pers.color}' {sw_time} секунды ")

            wait(sw_time)

            print(f"Светофор закончил гореть цветом '{pers.color}' " 
                  f"{(d_t.now() - start_state_time).seconds} секунды ")


if __name__ == '__main__':
    TrafficLight().burn()