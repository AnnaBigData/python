# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:41:07 2021

@author: Anna Ku
"""

 #3
    
number = int(input("Number 1-12: "))
if number <1 or number >12:
        print("error")
seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
for key in seasons.keys():
        if number in seasons[key]:
            print(key)