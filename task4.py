# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:41:08 2021

@author: Anna Ku
"""

           
#4 

string = input("Введите фразу: ")
word = []
num = 1
for i in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [i]}")
        num += 1
    else:
        print(f" {num} {word [i] [0:10]}")
        num += 1
        
