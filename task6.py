# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:59:09 2021

@author: Anna Ku
"""

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. 
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

x = int(input("Число старт: "))

def func1():
    y = range(x, x+10)
    for i in y:
        print(i)
 

def func2():
    for i in count(x,5): 
        if i >= 50:
            break
        else:
            print(i)
print(func2())

w = [2, 3, 10, 15]
q = 0

for el in cycle(w):
    if q > 20:
        break
    print(el)
    q += 1

