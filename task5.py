# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:33:06 2021

@author: Anna Ku
"""

# 5. Создать (программно) текстовый файл, записать в него программно 
# набор чисел, разделенных пробелами. Программа должна подсчитывать 
# сумму чисел в файле и выводить ее на экран.

import json

numbers=[1,2,3,4]

with open("file.json", 'w') as f:
    json.dump(numbers, f) 

with open("file.json", 'r') as f:
    numbers = json.load(f)

print(sum(numbers))