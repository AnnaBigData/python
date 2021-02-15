# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:10:06 2021

@author: Anna Ku
"""

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
#  и величину их окладов. Определить, кто из сотрудников имеет оклад менее 
#  20 тыс., вывести фамилии этих сотрудников. 
#  Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

with open('text3.txt', encoding='utf-8') as f:
    people = {}
    salaries = []

    for l in f:
        key, value = l.split(":")
        people[key] = value
        if int(value) < 20000:
            print(f'{key}: < 20000')
        salary = int(value)
        salaries.append(salary)
    print(round(mean(salaries), 2))
        