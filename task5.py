# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:41:53 2021

@author: Anna Ku
"""

# 5. Реализовать формирование списка, используя функцию range() 
# и возможности генератора. В список должны войти четные числа от 100 до 1000 
# (включая границы). Необходимо получить результат вычисления произведения всех
#  элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce
x = (i for i in range(100, 1001) if i % 2 ==0)

def product(prev_el, el):
    return prev_el * el
print(reduce(product, x))