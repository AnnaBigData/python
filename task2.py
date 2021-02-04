# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:41:06 2021

@author: Anna Ku
"""

 # 2.   
  

s = input('List, no blanks: ')
l = list(s)
if len(l) % 2==0:
    l[::2], l[1::2] = l[1::2], l[::2]
    print(l)
else:
    t=l[:-1]
    t[::2], t[1::2] = t[1::2], t[::2]
    t.append(l[-1])
    print (t)