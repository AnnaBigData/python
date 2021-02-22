# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:13:29 2021

@author: Anna Ku
"""

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
#  (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
#  расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы 
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения 
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
#  первый элемент первой строки первой матрицы складываем с первым
#  элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, rows, cols, val):
        self.matrixRC = [[val] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join(' | '.join(map(str, row)) for row in self.matrixRC)
    
    def __add__(self, other):
        matrixRC = [] 
        for j in range(len(self.matrixRC)):
            temp = []            
            for k in range(len(self.matrixRC[j])):
                x = self.matrixRC[j][k] + other.matrixRC[j][k]
                temp.append(x)
            matrixRC.append(temp)
            return matrixRC

m = Matrix(5, 3, 4)
m1 = Matrix (3, 3, 8)

print (m+m1)