# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:45:23 2021

@author: Anna Ku
"""

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

my_list = range(20, 241)
new_list = [el for el in my_list if el % 20 == 0 or el % 21==0]
print(new_list)