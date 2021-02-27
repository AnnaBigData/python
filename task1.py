# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:30:07 2021

@author: Anna Ku
"""

# Реализовать класс «Дата», функция-конструктор которого должна принимать
#  дату в виде строки формата «день-месяц-год». В рамках класса реализовать 
#  два метода. Первый, с декоратором @classmethod, должен извлекать число, 
#  месяц, год и преобразовывать их тип к типу «Число». 
#  Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
#  месяца и года (например, месяц — от 1 до 12). Проверить работу полученной 
#  структуры на реальных данных.

class Data:
  
    def __init__(self, dd, mm, yy):
        self.dd = dd 
        self.mm = mm
        self.yy = yy
        
    @classmethod
    def digitdata(cls, dd, mm, yy):
               print (f"{dd} : {mm} : {yy}")
                 
            
    @staticmethod
    def my_data_check(dd, mm, yy):
       if 1 <= dd <= 31:
           if 1 <= mm <= 12:
               if 0 <= yy <= 21:
                   return f"{dd} : {mm} : {yy}"
               else: 
                   raise ValueError("Задано неверное число")
           else:
                raise ValueError("Задано неверное число")
       else: 
            raise ValueError("Задано неверное число")
            
d = Data(5, 12, 20)
print(d.digitdata(6, 12, 20))
print(d.my_data_check(5, 12, 20))   