# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:22:31 2021

@author: Anna Ku
"""

# Реализовать проект «Операции с комплексными числами». Создайте класс 
# «Комплексное число», реализуйте перегрузку методов сложения и умножения 
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
#  (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#  Проверьте корректность полученного результата.

class Complex:
    def __init__(self, *args):
        self.a = complex(int(input("a: ")).real, imag=0.2)
        self.b = complex(int(input("b: ")))
        
    def plus(self):
          return self.a + self.b
    
    def mult(self):
        return self.a * self.b
    
c = Complex()
print (c.plus())
print (c.mult())
