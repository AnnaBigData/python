# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:27:05 2021

@author: Anna Ku
"""

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление./
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль./
 
def myfunc():
    a = int(input("Numbers a: "))
    b = int(input("Numbers b: "))
    if b==0:
        print ("error")
    return a/b
print(myfunc())
    

