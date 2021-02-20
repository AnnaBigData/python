# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:17:11 2021

@author: Anna Ku
"""

# Реализовать базовый класс Worker (работник), 
# в котором определить атрибуты: name, surname, position 
# (должность), income (доход). Последний атрибут должен быть 
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
#  на базе класса Worker. В классе Position реализовать
#  методы получения полного имени сотрудника (get_full_name) и 
#  дохода с учетом премии (get_total_income). 
#  Проверить работу примера на реальных данных
#  (создать экземпляры класса Position, передать данные,
#   проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name 
        self.surname = surname
        self.position = position 
        self._income = {'profit': wage, "bonus": bonus}
    
    
class Position (Worker):
     def get_full_name(self):
         return (self.name + " " + self.surname)
     
     def get_total_income(self):
        return (sum(self._income.values()))     
    
a = Position("Tim", "Cook", "CEO", 3000, 5000)
print(f'{a.get_full_name(), a.position, a.get_total_income()}')
