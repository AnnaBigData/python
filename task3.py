# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:00:42 2021

@author: Anna Ku
"""

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.

def func():
    a = int(input("1:" ))
    b = int(input("2:" ))
    c = int(input("3:" ))
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    elif c < a and c < b:
        return a + b
print(func())
    
def func1():
    a = int(input("1:" ))
    b = int(input("2:" ))
    c = int(input("3:" ))
    x = min(a,b,c)
    return (a + b + c) - (x)
print(func1())