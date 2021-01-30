# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:50:29 2021

@author: Anna Kutyrina
"""
# задание 1
a = 10 
b = 12
c = -5

print (a, b, c)

user_var1, user_var2, user_var3 = input("Введите 3 переменные: ").split() 
print("Первая переменная: ", user_var1)
print("Вторая переменная: ", user_var2)
print("Третья переменная : ", user_var3)
print()


var_x = list(map(int, input("Введите несколько чисел: ").split()))
print("Список переменных: ", var_x)

# задание 2 

time = int(input('Введите секунды:'))
hour = int(time // 3600)
minute = int((time % 3600) / 60)
second = int((time % 3600) % 60)
print(f'{hour:d}:{minute:d}:{second:d}')

# задание 3

n = int(input("Введите n: "))

temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
fin = n+int(t1)+int(t2)

print("Значение:", fin)

# задание 4 

value = input("Введите положительное число: ")
numbers = [int(y) for y in str(value)]
x = 1
lar = numbers[x]
while x < len(numbers):
  if numbers[x] > lar:
     lar = numbers[x]
  x = x+1
print (lar)


# задание 5 (установила нижнюю границу рентабельности в 5% для теста)

income = int(input('Введите показатель выручки:'))
expenses = int(input('Введите расходы:'))
profit = ((income - expenses)/income)*100

if income > expenses and profit > 5:
    print ('Норм, живем')
    staf = int(input('Число сотрудников:'))
    soul = (income - expenses) / staf
    profitf = '{:.2f}%'.format(profit)
    print ('Рентабельность равна: {}, на нос: {}'.format(profitf, soul))
    
elif expenses > income:
    print ('Так не пойдет, идите еще работайте')
    
elif expenses == income:
     print ('В ноль')
     
# задание 6 

day1_a = float(input('Пробежал в 1-й день, км:')) 
desired_b = float(input('Надо, км :'))
final = day1_a + day1_a*(0.1*x)          

while final <= desired_b:
    x = x + 1
    final = day1_a + (day1_a*(0.1*x))
print ('бежал {} дней'.format(x))
    
