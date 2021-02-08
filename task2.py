# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:41:34 2021

@author: Anna Ku
"""


# Реализовать функцию, принимающую несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, 
# email, телефон. 
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(**kwargs): 
    return kwargs

print (user(name="A", surname="B", year='1987', city="Moscow", email="a@b.com", phone="+7 916"))

def user1(**kwargs):
   return kwargs
    
print("\n")
print (user1(name='A', surname='B', year='1987', city='Moscow', email='a@b.com', phone='+7 916'))
print (user1(name='B', surname='C', year='1991', city='NY', email='c@d.ru', phone='+7 903'))

