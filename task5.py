# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:52:40 2021

@author: Anna Ku
"""

# Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса 
#  Pen (ручка), Pencil (карандаш), Handle (маркер). 
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение. 
#  Создать экземпляры классов и проверить, что выведет описанный метод
#  для каждого экземпляра.

class Stationery:
        def __init__(self, title):
            self.title = title
        def draw(self):
            print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
            print("ручка")
            
class Pencil(Stationery):
    def draw(self):
            print("карандаш")
            
class Handle(Stationery):
      def draw(self):
            print("маркер")
            
s = Stationery("Yes")
p = Pen("No")
Pp = Pencil("Maybe")
h = Handle("Perhaps")

s.draw()
p.draw()
Pp.draw()
h.draw()