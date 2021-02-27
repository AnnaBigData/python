# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:40:00 2021

@author: Anna Ku
"""

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем.
#  При вводе нуля в качестве делителя программа должна корректно 
#  обработать эту ситуацию и не завершиться с ошибкой.

class Data:
    def __init__(self, number, number2):       
        self.number = number
        self.number2 = number2
        
    def zero(self, number, number2):
       try:
           res = number/number2
       except ZeroDivisionError:
           print("На ноль делить нельзя")
       else:
           print(f"Все хорошо. Результат - {res}")
       finally:
              print("Программа завершена")

y = Data(15, 0)
print(y.zero(15, 0))
